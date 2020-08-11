# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# logger for mediaserver
# ------------------------------------------------------------
import logging
import logging.config
import os

import config


class ExtendedLogger(logging.Logger):
    def findCaller(self):
        f = logging.currentframe().f_back.f_back
        rv = "(unknown file)", 0, "(unknown function)"
        while hasattr(f, "f_code"):
            co = f.f_code
            filename = os.path.normcase(co.co_filename)
            if "logger" in filename:  # This line is modified.
                f = f.f_back
                continue
            filename = filename + " " + co.co_name
            rv = (filename, f.f_lineno, co.co_name)
            break
        return rv


logging.setLoggerClass(ExtendedLogger)
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)-5s %(asctime)s [%(filename)-40s] %(message)s',
                    datefmt="%d/%m/%y-%H:%M:%S",
                    filename=os.path.join(config.get_data_path(), "alfa.log"),
                    filemode='w')
logger_object = logging.getLogger("mediaserver")


def info(texto=""):
    if config.get_setting("debug"):
        logger_object.info(unicode(str(texto), "utf-8", "ignore").replace("\n", "\n" + " " * 67))


def debug(texto=""):
    if config.get_setting("debug"):
        logger_object.debug(unicode(str(texto), "utf-8", "ignore").replace("\n", "\n" + " " * 67))


def error(texto=""):
    logger_object.error(unicode(str(texto), "utf-8", "ignore").replace("\n", "\n" + " " * 67))


class WebErrorException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
