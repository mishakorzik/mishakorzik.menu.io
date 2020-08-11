# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Mediaserver Base controller
# ------------------------------------------------------------

import threading

from platformcode import config, platformtools


class Controller(object):
    pattern = ""
    name = None

    def __init__(self, handler=None, ID=None):

        self.handler = handler
        self.id = ID

        if not self.id:
            self.id = threading.current_thread().name

        if self.handler:
            self.platformtools = Platformtools()
            self.host = "http://%s:%s" % (config.get_local_ip(), config.get_setting("server.port"))

    def __setattr__(self, name, value):
        super(Controller, self).__setattr__(name, value)

        if name == "platformtools":
            platformtools.controllers[self.id] = self.platformtools

    def __del__(self):
        from platformcode import platformtools
        if self.id in platformtools.controllers:
            del platformtools.controllers[self.id]

    def run(self, path):
        pass

    def match(self, path):
        if self.pattern.findall(path):
            return True
        else:
            return False


class Platformtools(object):
    def dialog_ok(self, heading, line1, line2="", line3=""):
        pass

    def dialog_notification(self, heading, message, icon=0, time=5000, sound=True):
        pass

    def dialog_yesno(self, heading, line1, line2="", line3="", nolabel="No", yeslabel="Si", autoclose=""):
        return True

    def dialog_select(self, heading, list):
        pass

    def dialog_progress(self, heading, line1, line2="", line3=""):
        class Dialog(object):
            def __init__(self, heading, line1, line2, line3, PObject):
                self.PObject = PObject
                self.closed = False
                self.heading = heading
                text = line1
                if line2: text += "\n" + line2
                if line3: text += "\n" + line3

            def iscanceled(self):
                return self.closed

            def update(self, percent, line1, line2="", line3=""):
                pass

            def close(self):
                self.closed = True

        return Dialog(heading, line1, line2, line3, None)

    def dialog_progress_bg(self, heading, message=""):
        class Dialog(object):
            def __init__(self, heading, message, PObject):
                self.PObject = PObject
                self.closed = False
                self.heading = heading

            def isFinished(self):
                return not self.closed

            def update(self, percent=0, heading="", message=""):
                pass

            def close(self):
                self.closed = True

        return Dialog(heading, message, None)

    def dialog_input(self, default="", heading="", hidden=False):
        return default

    def dialog_numeric(self, type, heading, default=""):
        return None

    def itemlist_refresh(self):
        pass

    def itemlist_update(self, item):
        pass

    def render_items(self, itemlist, parentitem):
        pass

    def is_playing(self):
        return False

    def play_video(self, item):
        pass

    def show_channel_settings(self, list_controls=None, dict_values=None, caption="", callback=None, item=None,
                              custom_button=None, channelpath=None):
        pass

    def show_video_info(self, data, caption="Información del vídeo", callback=None, item=None):
        pass

    def show_recaptcha(self, key, url):
        pass
