"""This is the module that defines base page class.
"""

from logging import getLogger

import customtkinter as ctk

from lib.common.types import ParamLog
from lib.components.base import BaseComponent, EventBus

PARAM_LOG = ParamLog()
LOGGER = getLogger(PARAM_LOG.NAME)


class BasePage(ctk.CTkScrollableFrame, BaseComponent):
    """Defines the base page.

    Args:
        master (ctk.CTk): parent widget class.
        event_bus (EventBus): :class:`EventBus` class.
        page_name (str): page name.
    """
    def __init__(
            self,
            master: ctk.CTk,
            event_bus: EventBus,
            page_name: str,
            **kwargs,
        ) -> None:
        ctk.CTkScrollableFrame.__init__(self=self, master=master, **kwargs)
        BaseComponent.__init__(self=self, event_bus=event_bus)

        self.configure(fg_color='transparent')

        ctk.CTkLabel(
            master=self,
            text=page_name,
            text_color=['black', 'white'],
            fg_color=['gray80', 'gray20'],
            corner_radius=6,
        ).grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky=ctk.NSEW)
