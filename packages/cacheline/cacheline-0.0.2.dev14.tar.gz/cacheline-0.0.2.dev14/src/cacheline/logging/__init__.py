import logging
import sys
from typing import Callable, Optional
from urllib.parse import quote, urljoin

import colorlog
import requests
from pythonjsonlogger import jsonlogger

if sys.version_info >= (3, 12) and ("taskName" not in jsonlogger.RESERVED_ATTRS):
    jsonlogger.RESERVED_ATTRS = ("taskName", *jsonlogger.RESERVED_ATTRS)


_DEFAULT_FORMAT = "%(asctime)s %(name)s %(levelname)s %(process)d %(thread)d %(filename)s %(funcName)s %(levelno)s"


def getLogger(
    name: str,
    *,
    format: Optional[str] = None,
    handler: Optional[logging.Handler] = None,
):
    logger = logging.getLogger(name)
    logger.propagate = False
    if handler is None:
        handler = logging.StreamHandler(sys.stderr)
        formatter = jsonlogger.JsonFormatter(format or _DEFAULT_FORMAT)
        handler.setFormatter(formatter)
    else:
        if format is not None:
            formatter = jsonlogger.JsonFormatter(format)
            handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


class LoggerLaunchar(logging.Handler):
    def __init__(self, push_function: Callable[[str], None]):
        super().__init__()
        self._push_function = push_function

    def emit(self, record):
        self._push_function(self.format(record))

    def getLogger(self, name: str):
        logger = getLogger(name, handler=self, format=_DEFAULT_FORMAT)
        stream_handler = logging.StreamHandler(sys.stderr)
        stream_handler.setFormatter(
            colorlog.ColoredFormatter(
                "%(asctime)s %(log_color)s%(levelname)-8s%(reset)s %(message_log_color)s%(message)s %(reset)s%(pathname)s:%(lineno)d ",
                datefmt=None,
                reset=True,
                log_colors={
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "red,bg_white",
                },
                secondary_log_colors={
                    "message": {
                        "DEBUG": "cyan",
                        "INFO": "green",
                        "WARNING": "yellow",
                        "ERROR": "red",
                        "CRITICAL": "red,bg_white",
                    }
                },
                style="%",
            )
        )
        logger.addHandler(stream_handler)
        return logger


class WebdisLoggerLaunchar(LoggerLaunchar):
    def __init__(self, server: str, key: str):
        super().__init__(self.push)
        self._url = server
        self._key = quote(key)

    def push(self, row: str):
        requests.get(urljoin(self._url, f"LPUSH/{self._key}/{quote(row)}"))
