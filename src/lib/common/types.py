"""This is the module that defines the types.
"""

import enum
import logging
import zoneinfo

from pydantic import BaseModel, ConfigDict, Field

#: ZoneInfo class.
ZoneInfo = zoneinfo.ZoneInfo(key='Asia/Tokyo')


class ParamKey(enum.StrEnum):
    """Defines the dictionary key for the main parameters.
    """
    HANDLER = enum.auto()
    LEVEL = enum.auto()
    PARAM = enum.auto()
    RESULT = enum.auto()
    MODE = enum.auto()
    THEME = enum.auto()


class ParamLog(BaseModel):
    """Defines the parameters used in the logging configuration.
    """
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid',
    )
    #: str: The stream handler key.
    SH: str = Field(default='sh', frozen=True)
    #: str: The file handler key.
    FH: str = Field(default='fh', frozen=True)
    #: str: The name to pass to ``logging.getLogger``.
    NAME: str = Field(default='main')
    #: dict[str, bool]: The handler flag to use.
    HANDLER: dict[str, bool] = Field(
        default={
            'sh': True,
            'fh': True,
        },
    )
    #: dict[str, int]: The log level.
    LEVEL: dict[str, int] = Field(
        default={
            'sh': logging.DEBUG,
            'fh': logging.DEBUG,
        },
    )
    #: str: The file path.
    FPATH: str = Field(default='log/log.txt')
    #: int: The max file size.
    SIZE: int = Field(default=int(1e+6), gt=0)
    #: int: The number of files.
    NUM: int = Field(default=10, gt=0)


THEME_DATA_TYPE = dict[str, int | str | list[str] | dict[str, int | str]]


class SideBarFrameName(enum.StrEnum):
    """Defines the frame name of sidebar.
    """
    HEADER = enum.auto()
    MAIN = enum.auto()


class EventName(enum.StrEnum):
    """Defines the event name.
    """
    SHOW_PAGE = enum.auto()
    BUILD_PAGE = enum.auto()
    DEL_ALL_BUTTON = enum.auto()
    ADD_BUTTON = enum.auto()
    CHANGE_CONF = enum.auto()
    GET_DATA = enum.auto()
    RECIEVE_DATA = enum.auto()
