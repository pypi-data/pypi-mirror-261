""" hop.util
"""

import logging
import functools

import termcolor
import coloredlogs

blue = functools.partial(termcolor.colored, color="blue")
red = functools.partial(termcolor.colored, color="red")
green = functools.partial(termcolor.colored, color="green")
yellow = functools.partial(termcolor.colored, color="yellow")
bold = functools.partial(termcolor.colored, attrs=["bold"])


def get_logger(name):
    """
    utility function for returning a logger
    with standard formatting patterns, etc
    """

    class DuplicateFilter(logging.Filter):
        def filter(self, record):
            # add other fields if you need more granular comparison, depends on your app
            current_log = (record.module, record.levelno, record.msg)
            if current_log != getattr(self, "last_log", None):
                self.last_log = current_log
                return True
            return False

    formatter = coloredlogs.ColoredFormatter(
        fmt=" - ".join(
            [
                # "[%(asctime)s]",
                "%(levelname)s\t",
                "%(name)s\t",
                "%(message)s",
            ]
        ),
        # datefmt="%Y-%m-%d %H:%M:%S",
    )
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    if not logger.handlers:
        # prevents duplicate registration
        logger.addHandler(log_handler)
    logger.addFilter(DuplicateFilter())  # add the filter to it
    # FIXME: get this from some kind of global config
    logger.setLevel("DEBUG")
    return logger


LOGGER = get_logger(__name__)


def first(*items):
    """returns first item in iterable testing truthy"""
    for item in items:
        if item:
            return item
    return None


def tags_list_to_dict(tags: list) -> dict:
    """ """
    assert isinstance(tags, list), "expected list"
    tags = {t["Key"]: t["Value"] for t in tags}
    return tags
