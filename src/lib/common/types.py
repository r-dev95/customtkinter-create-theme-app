"""This is the module that defines the types.
"""

import enum

THEME_DATA_TYPE = dict[str, int | str | list[str] | dict[str, int | str]]


class ParamKey(enum.StrEnum):
    """Defines the dictionary key for the main parameters.
    """
    LEVEL = enum.auto()
    PARAM = enum.auto()
    RESULT = enum.auto()
    MODE = enum.auto()
    THEME = enum.auto()


class SideBarFrameName(enum.StrEnum):
    HEADER = enum.auto()
    MAIN = enum.auto()


class EventName(enum.StrEnum):
    SHOW_PAGE = enum.auto()
    BUILD_PAGE = enum.auto()
    DEL_ALL_BUTTON = enum.auto()
    ADD_BUTTON = enum.auto()
    CHANGE_CONF = enum.auto()
    GET_DATA = enum.auto()
    RECIEVE_DATA = enum.auto()
