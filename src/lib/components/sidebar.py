"""This is the module that defines sidebar component class.
"""
from collections.abc import Callable
from logging import getLogger

import customtkinter as ctk

from lib.common.types import EventName as E
from lib.common.types import ParamLog, SideBarFrameName
from lib.components.base import BaseComponent, EventBus

PARAM_LOG = ParamLog()
LOGGER = getLogger(PARAM_LOG.NAME)


class SideBar(ctk.CTkFrame, BaseComponent):
    """Define the sidebar component.
    """
    def __init__(self, master: ctk.CTk, event_bus: EventBus, **kwargs) -> None:
        ctk.CTkFrame.__init__(self=self, master=master, **kwargs)
        BaseComponent.__init__(self=self, event_bus=event_bus)

        self.configure(width=150)
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=1, weight=1)

        self.fg_color = 'transparent'
        self.hover_color = ('gray90', 'gray20')

        # Header Frame
        self.header_frame = ctk.CTkFrame(master=self, fg_color=self.fg_color)
        self.header_frame.grid(row=0, column=0, sticky=ctk.EW)
        self.header_frame.grid_columnconfigure(index=0, weight=1)
        self.switch_mode = ctk.CTkSwitch(
            master=self.header_frame,
            text='Light/Dark',
            command=self.on_switch_mode,
        )
        self.switch_mode.grid(row=0, column=0, padx=10, pady=10, sticky=ctk.EW)
        if ctk.get_appearance_mode() == 'Dark':
            self.switch_mode.select()

        # Main Frame
        self.main_frame = ctk.CTkScrollableFrame(master=self, fg_color=self.fg_color)
        self.main_frame.grid(row=1, column=0, sticky=ctk.NSEW)
        self.main_frame.grid_columnconfigure(index=0, weight=1)

        self.current_item: ctk.CTkButton = None
        self.sidebar_items: dict[str, ctk.CTkButton] = {}

    def register_events(self) -> dict[str, Callable]:
        """Returns a list of events to subscribe to.

        Returns:
            dict[str, Callable]: events list to register. (key: event name, val: func)
        """
        return {
            E.DEL_ALL_BUTTON: self.on_del_all_button,
            E.ADD_BUTTON: self.on_add_button,
            E.SHOW_PAGE: self.on_select_button,
        }

    def on_switch_mode(self) -> None:
        """Switch between light and dark mode.
        """
        if self.switch_mode.get():
            ctk.set_appearance_mode('dark')
        else:
            ctk.set_appearance_mode('light')

    def on_del_all_button(self, exclude_page_name: str) -> None:
        """Remove the sidebar all button.

        Args:
            exclude_page_name (str): Names of buttons to exclude from deletion.
        """
        for key in list(self.sidebar_items):
            if key != exclude_page_name:
                self.sidebar_items[key].destroy()
                del self.sidebar_items[key]

    def on_add_button(self, frame_name: SideBarFrameName, page_name: str) -> None:
        """Add the sidebar button.

        Args:
            frame_name (SideBarFrameName): The name of the frame to add the button to.
            page_name (str): The name of the button (corresponding to the page name).
        """
        if frame_name == SideBarFrameName.HEADER:
            master = self.header_frame
            index = len(self.header_frame.winfo_children())
        elif frame_name == SideBarFrameName.MAIN:
            master = self.main_frame
            index = len(self.sidebar_items)
        else:
            LOGGER.error(f'[frame_name] is wrong. {frame_name=}')
            raise ValueError

        self.sidebar_items[page_name] = ctk.CTkButton(
            master=master,
            height=40,
            fg_color=self.fg_color,
            hover_color=self.hover_color,
            text_color=('black', 'white'),
            anchor=ctk.W,
            text=page_name,
            command=lambda name=page_name: self.event_bus.emit(
                event_name=E.SHOW_PAGE,
                page_name=name,
            ),
        )
        self.sidebar_items[page_name].grid(row=index, column=0, sticky=ctk.EW)

    def on_select_button(self, page_name: str) -> None:
        """Change the color of the selected button.

        Args:
            page_name (str): The name of the button (corresponding to the page name).
        """
        if self.current_item is not None:
            self.current_item.configure(fg_color=self.fg_color)
        self.current_item = self.sidebar_items[page_name]
        self.current_item.configure(fg_color=self.hover_color)
