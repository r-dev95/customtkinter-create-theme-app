"""This is the module that defines Setting page class.
"""

import enum
from collections.abc import Callable
from logging import getLogger

import customtkinter as ctk

from lib.common.types import THEME_DATA_TYPE, ParamLog
from lib.common.types import EventName as E
from lib.components.base import BasePage, EventBus

PARAM_LOG = ParamLog()
LOGGER = getLogger(PARAM_LOG.NAME)

ENTRY_ITEM_TYPE = dict[str, ctk.CTkEntry | list[ctk.CTkEntry] | dict[str, ctk.CTkEntry]]


class M(enum.StrEnum):
    """Defines the mode identifier (light/dark).
    """
    LIGHT = enum.auto()
    DARK = enum.auto()


class C(enum.StrEnum):
    """Defines the condition identifier.
    """
    COLOR = enum.auto()
    NUMBER = enum.auto()
    FONT = enum.auto()


class SettingPage(BasePage):
    """Defines the Setting page.

    Args:
        master (ctk.CTk): parent widget class.
        event_bus (EventBus): :class:`EventBus` class.
        page_name (str): page name.
        values (THEME_DATA_TYPE): CustomTkinter theme data.
    """
    def __init__(
            self,
            master: ctk.CTk,
            event_bus: EventBus,
            page_name: str,
            values: THEME_DATA_TYPE,
            **kwargs,
        ) -> None:
        # [Attention]
        # self.master is used by the parent class CustomTkinter.
        self._master = master
        self.page_name = page_name

        super().__init__(
            master=master,
            event_bus=event_bus,
            page_name=page_name,
            **kwargs,
        )

        self.grid_columnconfigure(index=(0, 1, 2), weight=1)

        self._condtions = {
            C.COLOR: 'color',
            C.NUMBER: ['corner_radius', 'width', 'length', 'spacing'],
            C.FONT: ['macOS', 'Windows', 'Linux'],
        }

        self.entry_items: ENTRY_ITEM_TYPE = {}

        row = 0
        for key, val in values.items():
            ctk.CTkLabel(
                master=self,
                text=key,
                width=180,
                anchor=ctk.W,
            ).grid(row=row, column=0, padx=10, pady=5)

            if self._condtions[C.COLOR] in key:
                row = self.create_entry_color(key=key, val=val, row=row)
            elif any(k in key for k in self._condtions[C.NUMBER]):
                row = self.create_entry_number(key=key, val=val, row=row)
            elif key in self._condtions[C.FONT]:
                row = self.create_entry_font(key=key, val=val, row=row)
            else:
                LOGGER.error(f'[key] is wrong. {key=}')
                raise ValueError

        self.event_bus.emit(
            event_name=E.CHANGE_CONF,
            item_name=page_name,
            values=self.get_data(),
        )

    def register_events(self) -> dict[str, Callable]:
        """Returns a list of events to subscribe to.

        Returns:
            dict[str, Callable]: events list to register. (key: event name, val: func)
        """
        return {E.GET_DATA: self.on_get_data}

    def unset_global_var(self, name: str) -> None:
        """Unsets a variable set inside Tkinter.

            *   e.g., ctk.StringVar name

        Args:
            name (str): a variable set inside Tkinter.
        """
        try:
            self._master.globalunsetvar(name)
        except ctk.ctk_tk.tkinter.TclError:
            LOGGER.debug(f'{self._master=} does not have StringVar ({name=}).')

    def create_str_var(self, name: str, value: str) -> ctk.StringVar:
        """Creates a ctk.StringVar.

        Args:
            name (str): string variable name.
            value (str): value.

        Returns:
            ctk.StringVar: ctk.StringVar.
        """
        self.unset_global_var(name=name)
        str_var = ctk.StringVar(value=value, name=name)
        str_var.trace_add(mode='write', callback=self.on_trace_var)
        return str_var

    def create_entry_color(self, key: str, val: str | list[str], row: int) -> int:
        """Creates a ctk.CTkEntry that sets 'color'.

            *   The 1st ctk.CTkEntry is for light mode.
            *   The 2nd ctk.CTkEntry is for dark  mode.

        Args:
            key (str): Settings that include 'color'
            val (str | list[str]): Setting Value.
            row (int): The number of row.

        Returns:
            int: The number of row.
        """
        if isinstance(val, list):
            values = {M.LIGHT: val[0], M.DARK: val[1]}
        elif isinstance(val, str):
            values = {M.LIGHT: val, M.DARK: None}
        else:
            LOGGER.error(f'[val] must be str or list[str, str]. {key=}, {val=}')
            raise TypeError

        self.entry_items[key] = {
            M.LIGHT: ctk.CTkEntry(
                master=self,
                width=120,
                textvariable=self.create_str_var(
                    name=f'{self.page_name}-{key}-{M.LIGHT}',
                    value=values[M.LIGHT],
                ),
            ),
            M.DARK: ctk.CTkEntry(
                master=self,
                width=120,
                textvariable=self.create_str_var(
                    name=f'{self.page_name}-{key}-{M.DARK}',
                    value=values[M.DARK],
                ),
            ),
        }
        self.entry_items[key][M.LIGHT].grid(row=row, column=1, padx=10)
        self.entry_items[key][M.DARK].grid(row=row, column=2, padx=10)
        row += 1
        return row

    def create_entry_number(self, key: str, val: str, row: int) -> int:
        """Creates a ctk.CTkEntry that sets 'number'.

            *   Set the items including one of the following.

                *   'corner_radius'
                *   'width'
                *   'length'
                *   'spacing'

        Args:
            key (str): Settings that include 'color'
            val (str | list[str]): Setting Value.
            row (int): The number of row.

        Returns:
            int: The number of row.
        """
        self.entry_items[key] = ctk.CTkEntry(
            master=self,
            width=120,
            textvariable=self.create_str_var(
                name=f'{self.page_name}-{key}-none',
                value=val,
            ),
        )
        self.entry_items[key].grid(row=row, column=1, padx=10)
        row += 1
        return row

    def create_entry_font(self, key: str, val: dict[str, int | str], row: int) -> int:
        """Creates a ctk.CTkEntry that sets 'font'.

            *   Set the items including one of the following.
            *   Also, set the following items separately for Windows, macOS, and Linux.

                *   'family'
                *   'size'
                *   'weight'

        Args:
            key (str): Settings that include 'color'
            val (str | list[str]): Setting Value.
            row (int): The number of row.

        Returns:
            int: The number of row.
        """
        self.entry_items[key] = {}
        for k, v in val.items():
            ctk.CTkLabel(
                master=self,
                text=k,
                width=120,
                anchor=ctk.W,
            ).grid(row=row, column=1, padx=10, pady=5)

            self.entry_items[key][k] = ctk.CTkEntry(
                master=self,
                width=120,
                textvariable=self.create_str_var(
                    name=f'{self.page_name}-{key}-{k}',
                    value=v,
                ),
            )
            self.entry_items[key][k].grid(row=row, column=2, padx=10)
            row += 1
        return row

    def get_data(self) -> THEME_DATA_TYPE:
        """Gets the setting values of all ctk.CTkEntry in the page.

        Returns:
            THEME_DATA_TYPE: setting values.
        """
        data = {}
        for key, val in self.entry_items.items():
            if self._condtions[C.COLOR] in key:
                data[key] = [val[M.LIGHT].get(), val[M.DARK].get()]
                if not data[key][0] or not data[key][1]:
                    data[key] = data[key][0] or data[key][1]
                if data[key][0] == data[key][1]:
                    data[key] = data[key][0]
            elif any(k in key for k in self._condtions[C.NUMBER]):
                try:
                    data[key] = int(val.get())
                except ValueError:
                    LOGGER.exception(f'{val=} must be number. ({key=})')
            elif any(k in key for k in self._condtions[C.FONT]):
                data[key] = {}
                for k, v in val.items():
                    try:
                        data[key][k] = int(v.get())
                    except ValueError:
                        data[key][k] = str(v.get())
            else:
                LOGGER.error(f'{key=} do not support.')
                raise ValueError
        return data

    def on_trace_var(self, *args: tuple[str]) -> None:
        """Watch for changes to setting values and change the widget configuration.
        """
        LOGGER.debug(f'{args=}')
        item_name = args[0].split('-')[0]

        self.event_bus.emit(
            event_name=E.CHANGE_CONF,
            item_name=item_name,
            values=self.get_data(),
        )

    def on_get_data(self) -> None:
        """Get the setting value and send it to HomePage.
        """
        self.event_bus.emit(
            event_name=E.RECIEVE_DATA,
            fm=self.page_name,
            data=self.get_data(),
        )
