""" hop.util
"""

from ssm.util import get_logger

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
