# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Parámetros de configuración (Server)
# ------------------------------------------------------------

import os
import re
import sys

PLATFORM_NAME = "Server"
PLUGIN_NAME = "Server"

settings_dic = {}
adult_setting = {}


def get_addon_version(linea_inicio=0, total_lineas=2, with_fix=False):
    '''
    Devuelve el número de de versión del addon, obtenido desde el archivo addon.xml
    '''
    path = os.path.join(get_runtime_path(), "addon.xml")
    f = open(path, "rb")
    data = []
    for x, line in enumerate(f):
        if x < linea_inicio: continue
        if len(data) == total_lineas: break
        data.append(line)
    f.close()
    data1 = "".join(data)
    # <addon id="plugin.video.alfa" name="Alfa" version="2.5.21" provider-name="Alfa Addon">
    aux = re.findall('<addon id="plugin.video.alfa" name="Alfa" version="([^"]+)"', data1, re.MULTILINE | re.DOTALL)
    version = "???"
    if len(aux) > 0:
        version = aux[0]
    return version


def get_platform(full_version=False):
    # full_version solo es util en xbmc/kodi
    ret = {
        'num_version': 1.0,
        'name_version': PLATFORM_NAME,
        'video_db': "",
        'plaform': PLATFORM_NAME
    }

    if full_version:
        return ret
    else:
        return PLATFORM_NAME


def is_xbmc():
    return False


def get_videolibrary_support():
    return True


def get_system_platform():
    """ fonction: pour recuperer la platform que xbmc tourne """
    platform = "unknown"
    if sys.platform == "linux" or sys.platform == "linux2":
        platform = "linux"
    elif sys.platform == "darwin":
        platform = "osx"
    elif sys.platform == "win32":
        platform = "windows"

    return platform


def open_settings():
    options = []
    from xml.dom import minidom
    settings = open(menufilepath, 'rb').read()
    xmldoc = minidom.parseString(settings)
    for category in xmldoc.getElementsByTagName("category"):
        for setting in category.getElementsByTagName("setting"):
            options.append(dict(setting.attributes.items() + [(u"category", category.getAttribute("label")),
                                                              (u"value", get_setting(setting.getAttribute("id")))]))

    from platformcode import platformtools
    global adult_setting
    adult_password = get_setting('adult_password')
    if not adult_password:
        adult_password = set_setting('adult_password', '0000')
    adult_mode = get_setting('adult_mode')
    adult_request_password = get_setting('adult_request_password')

    platformtools.open_settings(options)

    # Hemos accedido a la seccion de Canales para adultos
    if get_setting('adult_aux_intro_password'):
        # La contraseña de acceso es correcta
        if get_setting('adult_aux_intro_password') == adult_password:

            # Cambio de contraseña
            if get_setting('adult_aux_new_password1'):
                if get_setting('adult_aux_new_password1') == get_setting('adult_aux_new_password2'):
                    set_setting('adult_password', get_setting('adult_aux_new_password1'))
                else:
                    platformtools.dialog_ok("Canales para adultos",
                                            "Los campos 'Nueva contraseña' y 'Confirmar nueva contraseña' no coinciden."
                                            , "Entre de nuevo en 'Preferencias' para cambiar la contraseña")

        else:
            platformtools.dialog_ok("Canales para adultos", "La contraseña no es correcta.",
                                    "Los cambios realizados en esta sección no se guardaran.")
            # Deshacer cambios
            set_setting("adult_mode", adult_mode)
            set_setting("adult_request_password", adult_request_password)

        # Borramos settings auxiliares
        set_setting('adult_aux_intro_password', '')
        set_setting('adult_aux_new_password1', '')
        set_setting('adult_aux_new_password2', '')


def get_setting(name, channel="", server="", default=None):
    """
    Retorna el valor de configuracion del parametro solicitado.

    Devuelve el valor del parametro 'name' en la configuracion global, en la configuracion propia del canal 'channel'
    o en la del servidor 'server'.

    Los parametros channel y server no deben usarse simultaneamente. Si se especifica el nombre del canal se devolvera
    el resultado de llamar a channeltools.get_channel_setting(name, channel, default). Si se especifica el nombre del
    servidor se devolvera el resultado de llamar a servertools.get_channel_setting(name, server, default). Si no se
    especifica ninguno de los anteriores se devolvera el valor del parametro en la configuracion global si existe o
    el valor default en caso contrario.

    @param name: nombre del parametro
    @type name: str
    @param channel: nombre del canal
    @type channel: str
    @param server: nombre del servidor
    @type server: str
    @param default: valor devuelto en caso de que no exista el parametro name
    @type default: any

    @return: El valor del parametro 'name'
    @rtype: any

    """

    # Specific channel setting
    if channel:

        # logger.info("config.get_setting reading channel setting '"+name+"' from channel json")
        from core import channeltools
        value = channeltools.get_channel_setting(name, channel, default)
        # logger.info("config.get_setting -> '"+repr(value)+"'")

        return value

    elif server:
        # logger.info("config.get_setting reading server setting '"+name+"' from server json")
        from core import servertools
        value = servertools.get_server_setting(name, server, default)
        # logger.info("config.get_setting -> '"+repr(value)+"'")

        return value

    # Global setting
    else:
        # logger.info("config.get_setting reading main setting '"+name+"'")
        global settings_dic
        value = settings_dic.get(name, default)
        if value == default:
            return value

        # logger.info("config.get_setting -> '"+value+"'")
        # hack para devolver el tipo correspondiente
        if value == "true":
            return True
        elif value == "false":
            return False
        else:
            # special case return as str
            if name in ["adult_password", "adult_aux_intro_password", "adult_aux_new_password1",
                        "adult_aux_new_password2"]:
                return value
            else:
                try:
                    value = int(value)
                except ValueError:
                    pass

                return value


def set_setting(name, value, channel="", server=""):
    """
    Fija el valor de configuracion del parametro indicado.

    Establece 'value' como el valor del parametro 'name' en la configuracion global o en la configuracion propia del
    canal 'channel'.
    Devuelve el valor cambiado o None si la asignacion no se ha podido completar.

    Si se especifica el nombre del canal busca en la ruta \addon_data\plugin.video.alfa\settings_channels el
    archivo channel_data.json y establece el parametro 'name' al valor indicado por 'value'. Si el archivo
    channel_data.json no existe busca en la carpeta channels el archivo channel.xml y crea un archivo channel_data.json
    antes de modificar el parametro 'name'.
    Si el parametro 'name' no existe lo añade, con su valor, al archivo correspondiente.


    Parametros:
    name -- nombre del parametro
    value -- valor del parametro
    channel [opcional] -- nombre del canal

    Retorna:
    'value' en caso de que se haya podido fijar el valor y None en caso contrario

    """
    if channel:
        from core import channeltools
        return channeltools.set_channel_setting(name, value, channel)
    elif server:
        from core import servertools
        return servertools.set_server_setting(name, value, server)
    else:
        global settings_dic

        if isinstance(value, bool):
            if value:
                value = "true"
            else:
                value = "false"
        elif isinstance(value, (int, long)):
            value = str(value)

        settings_dic[name] = value
        from xml.dom import minidom
        # Crea un Nuevo XML vacio
        new_settings = minidom.getDOMImplementation().createDocument(None, "settings", None)
        new_settings_root = new_settings.documentElement

        for key in settings_dic:
            nodo = new_settings.createElement("setting")
            nodo.setAttribute("value", settings_dic[key])
            nodo.setAttribute("id", key)
            new_settings_root.appendChild(nodo)

        fichero = open(configfilepath, "w")
        fichero.write(new_settings.toprettyxml(encoding='utf-8'))
        fichero.close()
        return value


def get_localized_string(code):
    translationsfile = open(TRANSLATION_FILE_PATH, "r")
    translations = translationsfile.read()
    translationsfile.close()
    cadenas = re.findall('msgctxt\s*"#%s"\nmsgid\s*"(.*?)"\nmsgstr\s*"(.*?)"' % code, translations)

    if len(cadenas) > 0:
        dev = cadenas[0][1]
        if not dev:
            dev = cadenas[0][0]
    else:
        dev = "%d" % code

    try:
        dev = dev.encode("utf-8")
    except:
        pass

    return dev


def get_localized_category(categ):
    categories = {'movie': get_localized_string(30122), 'tvshow': get_localized_string(30123),
                  'anime': get_localized_string(30124), 'documentary': get_localized_string(30125),
                  'vos': get_localized_string(30136), 'adult': get_localized_string(30126),
                  'direct': get_localized_string(30137), 'torrent': get_localized_string(70015)}
    return categories[categ] if categ in categories else categ


def get_videolibrary_path():
    value = get_setting("videolibrarypath")
    if value == "":
        verify_directories_created()
        value = get_setting("videolibrarypath")

    return value


def get_temp_file(filename):
    import tempfile
    return os.path.join(tempfile.gettempdir(), filename)


def get_runtime_path():
    return os.getcwd()


def get_data_path():
    dev = os.path.join(os.path.expanduser("~"), ".alfa")

    # Crea el directorio si no existe
    if not os.path.exists(dev):
        os.makedirs(dev)

    return dev


def get_cookie_data():
    import os
    ficherocookies = os.path.join(get_data_path(), 'cookies.dat')

    cookiedatafile = open(ficherocookies, 'r')
    cookiedata = cookiedatafile.read()
    cookiedatafile.close()

    return cookiedata


# Test if all the required directories are created
def verify_directories_created():
    from platformcode import logger
    from core import filetools

    config_paths = [["videolibrarypath", "library"],
                    ["downloadpath", "downloads"],
                    ["downloadlistpath", "downloads/list"],
                    ["bookmarkpath", "favorites"],
                    ["settings_path", "settings_channels"]]

    for path, default in config_paths:
        saved_path = get_setting(path)
        if not saved_path:
            saved_path = filetools.join(get_data_path(), *default.split("/"))
            set_setting(path, saved_path)

        if not filetools.exists(saved_path):
            logger.debug("Creating %s: %s" % (path, saved_path))
            filetools.mkdir(saved_path)

    config_paths = [["folder_movies", "CINE"],
                    ["folder_tvshows", "SERIES"]]

    for path, default in config_paths:
        saved_path = get_setting(path)

        if not saved_path:
            saved_path = default
            set_setting(path, saved_path)

        content_path = filetools.join(get_videolibrary_path(), saved_path)
        if not filetools.exists(content_path):
            logger.debug("Creating %s: %s" % (path, content_path))

            # si se crea el directorio
            filetools.mkdir(content_path)


def get_local_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 53))  # connecting to a UDP address doesn't send packets
    myip = s.getsockname()[0]
    return myip


def load_settings():
    global settings_dic
    defaults = {}
    from xml.etree import ElementTree

    # Lee el archivo XML (si existe)
    if os.path.exists(configfilepath):
        settings = open(configfilepath, 'rb').read()
        root = ElementTree.fromstring(settings)
        for target in root.findall("setting"):
            settings_dic[target.get("id")] = target.get("value")

    defaultsettings = open(menufilepath, 'rb').read()
    root = ElementTree.fromstring(defaultsettings)
    for category in root.findall("category"):
        for target in category.findall("setting"):
            if target.get("id"):
                defaults[target.get("id")] = target.get("default")

    for key in defaults:
        if key not in settings_dic:
            settings_dic[key] = defaults[key]
    set_settings(settings_dic)


def set_settings(JsonRespuesta):
    for Ajuste in JsonRespuesta:
        settings_dic[Ajuste] = JsonRespuesta[Ajuste].encode("utf8")
    from xml.dom import minidom
    # Crea un Nuevo XML vacio
    new_settings = minidom.getDOMImplementation().createDocument(None, "settings", None)
    new_settings_root = new_settings.documentElement

    for key in settings_dic:
        nodo = new_settings.createElement("setting")
        nodo.setAttribute("value", settings_dic[key])
        nodo.setAttribute("id", key)
        new_settings_root.appendChild(nodo)

    fichero = open(configfilepath, "w")
    fichero.write(new_settings.toprettyxml(encoding='utf-8'))
    fichero.close()


# Fichero de configuración
menufilepath = os.path.join(get_runtime_path(), "resources", "settings.xml")
configfilepath = os.path.join(get_data_path(), "settings.xml")
if not os.path.exists(get_data_path()):
    os.mkdir(get_data_path())
load_settings()
TRANSLATION_FILE_PATH = os.path.join(get_runtime_path(), "resources", "language", settings_dic["mediaserver_language"], "strings.po")

# modo adulto:
# sistema actual 0: Nunca, 1:Siempre, 2:Solo hasta que se reinicie sesión
# si es == 2 lo desactivamos.
if get_setting("adult_mode") == 2:
    set_setting("adult_mode", 0)
