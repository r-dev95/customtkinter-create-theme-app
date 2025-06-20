"""This is the module that defines Home page class.
"""

import json
from collections.abc import Callable
from logging import getLogger
from pathlib import Path

import customtkinter as ctk

from lib.common.file import dump_json, load_json
from lib.common.types import EventName as E
from lib.common.types import ParamLog
from lib.components.base import BasePage, EventBus

PARAM_LOG = ParamLog()
LOGGER = getLogger(PARAM_LOG.NAME)

FIRST_PAGE_NAME = 'Home'


class HomePage(BasePage):
    """Defines the Home page.

    Args:
        master (ctk.CTk): parent widget class.
        event_bus (EventBus): :class:`EventBus` class.
    """
    def __init__(self, master: ctk.CTk, event_bus: EventBus, **kwargs) -> None:
        super().__init__(
            master=master,
            event_bus=event_bus,
            page_name=FIRST_PAGE_NAME,
            **kwargs,
        )

        self.grid_columnconfigure(index=0, weight=1)

        self.base_file = ctk.CTkEntry(
            master=self,
            placeholder_text='テーマファイルを選択してください',
        )
        self.base_file.grid(row=0, column=0, padx=10, pady=10, sticky=ctk.EW)
        ctk.CTkButton(
            master=self,
            text='選択',
            command=self.on_open_file_dialog,
        ).grid(row=0, column=1, padx=(0, 10), pady=10)
        self.base_data = ctk.CTkTextbox(master=self, corner_radius=10, border_width=2)
        self.base_data.grid(row=1, column=0, padx=10, pady=10, sticky=ctk.NSEW)

        self.save_file = ctk.CTkEntry(
            master=self,
            placeholder_text='保存するファイルを選択してください',
        )
        self.save_file.grid(row=2, column=0, padx=10, pady=10, sticky=ctk.EW)
        ctk.CTkButton(
            master=self,
            text='保存',
            command=self.on_save_file,
        ).grid(row=2, column=1, padx=(0, 10), pady=10, sticky=ctk.N)
        self.save_data = ctk.CTkTextbox(master=self, corner_radius=10, border_width=2)
        self.save_data.grid(row=3, column=0, padx=10, pady=10, sticky=ctk.NSEW)

        self.new_data = {}

    def register_events(self) -> dict[str, Callable]:
        """Returns a list of events to subscribe to.

        Returns:
            dict[str, Callable]: events list to register. (key: event name, val: func)
        """
        return {
            E.RECIEVE_DATA: self.on_recieve_data,
        }

    def load_file(self, filepath: str) -> None:
        """Load CustomTkinter theme file.

        Args:
            filepath (str): file path.
        """
        data = load_json(fpath=Path(filepath))
        formated_data = json.dumps(data, indent=2, ensure_ascii=False)
        self.base_data.configure(state=ctk.NORMAL)
        self.base_data.delete(index1='1.0', index2=ctk.END)
        self.base_data.insert(index='1.0', text=formated_data)
        self.base_data.configure(state=ctk.DISABLED)
        self.event_bus.emit(event_name=E.BUILD_PAGE, data=data)

    def on_open_file_dialog(self) -> None:
        """Opens a file dialog to select the CustomTkinter theme file.
        """
        fpath = ctk.filedialog.askopenfilename(
            title='select theme json file.',
            filetypes=[('json file', '*.json')],
            initialdir=Path(__file__).parent.parent.parent.parent.absolute() /
            '.venv\\Lib\\site-packages\\customtkinter\\assets\\themes',
        )
        if fpath:
            self.base_file.configure(state=ctk.NORMAL)
            self.base_file.delete(first_index=0, last_index=ctk.END)
            self.base_file.insert(index=0, string=fpath)
            self.base_file.configure(state='readonly')
            self.load_file(filepath=fpath)

    def on_save_file(self) -> None:
        """Opens a file dialog to save the CustomTkinter theme file.
        """
        self.event_bus.emit(event_name=E.GET_DATA)
        formated_data = json.dumps(self.new_data, indent=2, ensure_ascii=False)
        self.save_data.configure(state=ctk.NORMAL)
        self.save_data.delete(index1='1.0', index2=ctk.END)
        self.save_data.insert(index='1.0', text=formated_data)
        self.save_data.configure(state=ctk.DISABLED)

        fpath = ctk.filedialog.asksaveasfilename(
            title='select save json file.',
            filetypes=[('json file', '*.json')],
            initialdir=Path(__file__).parent.parent.parent.absolute(),
        )
        if fpath:
            self.save_file.configure(state=ctk.NORMAL)
            self.save_file.delete(first_index=0, last_index=ctk.END)
            self.save_file.insert(index=0, string=fpath)
            self.save_file.configure(state='readonly')
            fpath = Path(fpath)
            dump_json(data=self.new_data, fpath=fpath, indent=2, ensure_ascii=False)

    def on_recieve_data(self, fm: str, data: dict[str, int | str | list[str]]) -> None:
        """Receive data.

        Args:
            fm (str): Sender name.
            data (dict[str, int  |  str  |  list[str]]): CustomTkinter theme data.
        """
        self.new_data[fm] = data
