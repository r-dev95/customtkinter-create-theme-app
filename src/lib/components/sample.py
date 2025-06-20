"""This is the module that defines Sample page class.
"""

import enum
import platform
from collections.abc import Callable
from logging import getLogger

import customtkinter as ctk

from lib.common.types import THEME_DATA_TYPE, ParamLog
from lib.common.types import EventName as E
from lib.components.base import BasePage, EventBus

PARAM_LOG = ParamLog()
LOGGER = getLogger(PARAM_LOG.NAME)

SAMPLE_ITEM_TYPE = dict[str,
    ctk.CTk |
    ctk.CTkToplevel |
    ctk.CTkFrame |
    ctk.CTkButton |
    ctk.CTkLabel |
    ctk.CTkEntry |
    ctk.CTkCheckBox |
    ctk.CTkSwitch |
    ctk.CTkRadioButton |
    ctk.CTkProgressBar |
    ctk.CTkSlider |
    ctk.CTkOptionMenu |
    ctk.CTkComboBox |
    ctk.CTkScrollbar |
    ctk.CTkSegmentedButton |
    ctk.CTkTextbox |
    ctk.CTkScrollableFrame |
    ctk.CTkFont |
    dict[str, ctk.CTkOptionMenu | ctk.CTkComboBox],
]


class W(enum.StrEnum):
    """Defines the CustomTkinter widget identifier.
    """
    CTK = 'CTk'
    TOPLEVEL = 'CTkToplevel'
    FRAME = 'CTkFrame'
    BUTTON = 'CTkButton'
    LABEL = 'CTkLabel'
    ENTRY = 'CTkEntry'
    CHECKBOX = 'CTkCheckBox'
    SWITCH = 'CTkSwitch'
    RADIOBUTTON = 'CTkRadioButton'
    PROGRESSBAR = 'CTkProgressBar'
    SLIDER = 'CTkSlider'
    OPTIONMENU = 'CTkOptionMenu'
    COMBOBOX = 'CTkComboBox'
    SCROLLBAR = 'CTkScrollbar'
    SEGMENTEDBUTTON = 'CTkSegmentedButton'
    TEXTBOX = 'CTkTextbox'
    SCROLLABLEFRAME = 'CTkScrollableFrame'
    FONT = 'CTkFont'
    DROPDOWNMENU = 'DropdownMenu'


class S(enum.StrEnum):
    """Defines the CustomTkinter widget setting identifier.
    """
    # Color
    FG_COLOR = enum.auto()
    TOP_FG_COLOR = enum.auto()
    LABEL_FG_COLOR = enum.auto()
    BORDER_COLOR = enum.auto()
    HOVER_COLOR = enum.auto()
    CHECKMARK_COLOR = enum.auto()
    PROGRESS_COLOR = enum.auto()
    BUTTON_COLOR = enum.auto()
    BUTTON_HOVER_COLOR = enum.auto()
    TEXT_COLOR = enum.auto()
    TEXT_COLOR_DISABLED = enum.auto()
    PLACEHOLDER_TEXT_COLOR = enum.auto()
    SELECTED_COLOR = enum.auto()
    SELECTED_HOVER_COLOR = enum.auto()
    UNSELECTED_COLOR = enum.auto()
    UNSELECTED_HOVER_COLOR = enum.auto()
    SCROLLBAR_BUTTON_COLOR = enum.auto()
    SCROLLBAR_BUTTON_HOVER_COLOR = enum.auto()
    # Width, Spacing, Radiius, length
    BORDER_WIDTH = enum.auto()
    BORDER_WIDTH_CHECKED = enum.auto()
    BORDER_WIDTH_UNCHECKED = enum.auto()
    BORDER_SPACING = enum.auto()
    CORNER_RADIUS = enum.auto()
    BUTTON_CORNER_RADIUS = enum.auto()
    BUTTON_LENGTH = enum.auto()
    # Font
    FAMILY = enum.auto()
    SIZE = enum.auto()
    WEIGHT = enum.auto()


class C(enum.StrEnum):
    """Defines the condition identifier.
    """
    FONT = enum.auto()
    DISABLED = enum.auto()


class SamplePage(BasePage):
    """Defines the Sample page.

    Args:
        master (ctk.CTk): parent widget class.
        event_bus (EventBus): :class:`EventBus` class.
    """
    def __init__(self, master: ctk.CTk, event_bus: EventBus, **kwargs) -> None:
        super().__init__(
            master=master,
            event_bus=event_bus,
            page_name='Sample',
            **kwargs,
        )

        self.grid_columnconfigure(index=(0, 1), weight=1)

        self._condtion = {
            C.FONT: [W.TOPLEVEL, W.PROGRESSBAR, W.SLIDER, W.FRAME, W.SCROLLBAR,
                     W.SCROLLABLEFRAME],
            C.DISABLED: [W.BUTTON, W.CHECKBOX, W.SWITCH, W.RADIOBUTTON, W.OPTIONMENU,
                         W.COMBOBOX, W.SEGMENTEDBUTTON],
        }

        self.sample_items: SAMPLE_ITEM_TYPE = {}

        frame = ctk.CTkFrame(master=self, fg_color=('gray80', 'gray20'))
        frame.grid(row=0, column=0, columnspan=2, sticky=ctk.EW)
        frame.grid_columnconfigure(index=(0, 1), weight=1)
        ctk.CTkButton(
            master=frame,
            text='Open Top Level Window',
            text_color=['black', 'black'],
            fg_color=['orange', 'orange'],
            hover_color=['orange3', 'orange3'],
            command=self.on_open_window,
        ).grid(row=0, column=0, pady=10)
        self.disabled_switch = ctk.CTkSwitch(
            master=frame,
            text='Disabled Sample',
            button_color=('orange', 'orange'),
            button_hover_color=('orange3', 'orange3'),
            progress_color=('orange3', 'orange3'),
            command=self.on_disabled_sample,
        )
        self.disabled_switch.grid(row=0, column=1, pady=20)

        # CTk
        # [Attetion]
        # Since more than one CTk cannot be started, it sets itself(master).
        self.sample_items[W.CTK] = master
        # CTkToplevel
        # [Attetion]
        # Press the button to launch CTkToplevel.

        # CTkLabel
        self.sample_items[W.LABEL] = ctk.CTkLabel(master=self)
        self.sample_items[W.LABEL].grid(row=1, column=0, pady=10)
        # CTkEntry
        self.sample_items[W.ENTRY] = ctk.CTkEntry(master=self)
        self.sample_items[W.ENTRY].grid(row=1, column=1, pady=10)
        # CTkButton
        self.sample_items[W.BUTTON] = ctk.CTkButton(master=self)
        self.sample_items[W.BUTTON].grid(row=2, column=0, pady=10)
        # CTkSegmentedButton
        self.sample_items[W.SEGMENTEDBUTTON] = ctk.CTkSegmentedButton(
            master=self,
            values=['button1', 'button2', 'button3'],
        )
        self.sample_items[W.SEGMENTEDBUTTON].grid(row=2, column=1, pady=10)
        # CTkCheckBox
        self.sample_items[W.CHECKBOX] = ctk.CTkCheckBox(master=self)
        self.sample_items[W.CHECKBOX].grid(row=3, column=0, pady=10)
        # CTkRadioButton
        self.sample_items[W.RADIOBUTTON] = ctk.CTkRadioButton(master=self)
        self.sample_items[W.RADIOBUTTON].grid(row=3, column=1, pady=10)
        # CTkSwitch
        self.sample_items[W.SWITCH] = ctk.CTkSwitch(master=self)
        self.sample_items[W.SWITCH].grid(row=4, column=0, pady=10)
        # CTkProgressBar
        self.sample_items[W.PROGRESSBAR] = ctk.CTkProgressBar(master=self)
        self.sample_items[W.PROGRESSBAR].grid(row=5, column=0, pady=10)
        # CTkSlider
        self.sample_items[W.SLIDER] = ctk.CTkSlider(master=self)
        self.sample_items[W.SLIDER].grid(row=5, column=1, pady=10)
        # CTkOptionMenu
        self.sample_items[W.OPTIONMENU] = ctk.CTkOptionMenu(
            master=self,
            values=['option1', 'option2', 'option3'],
        )
        self.sample_items[W.OPTIONMENU].grid(row=6, column=0, pady=10)
        # CTkComboBox
        self.sample_items[W.COMBOBOX] = ctk.CTkComboBox(
            master=self,
            values=['combo1', 'combo2', 'combo3'],
        )
        self.sample_items[W.COMBOBOX].grid(row=6, column=1, pady=10)
        # CTkTextbox
        self.sample_items[W.TEXTBOX] = ctk.CTkTextbox(master=self)
        self.sample_items[W.TEXTBOX].grid(row=7, column=0, columnspan=2, pady=10)
        # DropdownMenu
        # [Attetion]
        # DropdownMenu is used by CTkOptionMenu and CTkComboBox, so set both.
        self.sample_items[W.DROPDOWNMENU] = {
            W.OPTIONMENU: self.sample_items[W.OPTIONMENU]._dropdown_menu,  # noqa: SLF001
            W.COMBOBOX: self.sample_items[W.COMBOBOX]._dropdown_menu,  # noqa: SLF001
        }
        # [Attention]
        # Since CTkScrollableFrame is composed of CTkScrollbar and CTkFrame, CTkLabel,
        # set each of these classes.
        # CTkScrollableFrame
        self.sample_items[W.SCROLLABLEFRAME] = self
        # CTkScrollbar
        self.sample_items[W.SCROLLBAR] = self._scrollbar
        # CTkFrame
        self.sample_items[W.FRAME] = self._parent_frame

    def register_events(self) -> dict[str, Callable]:
        """Returns a list of events to subscribe to.

        Returns:
            dict[str, Callable]: events list to register. (key: event name, val: func)
        """
        return {E.CHANGE_CONF: self.on_change_conf}

    def on_open_window(self) -> None:
        """Open ctk.CTkToplevel window.
        """
        if (W.TOPLEVEL not in self.sample_items
            or not self.sample_items[W.TOPLEVEL].winfo_exists()
            ):
            self.sample_items[W.TOPLEVEL] = ctk.CTkToplevel(master=self)
            self.sample_items[W.TOPLEVEL].attributes('-topmost', True)  # noqa: FBT003
            self.sample_items[W.TOPLEVEL].grid_columnconfigure(index=0, weight=1)
            ctk.CTkLabel(
                master=self.sample_items[W.TOPLEVEL],
                text='CTkToplevel Window',
            ).grid(row=0, column=0, padx=50, pady=50, sticky=ctk.EW)

    def on_disabled_sample(self) -> None:
        state = 'normal' if not self.disabled_switch.get() else 'disabled'
        for key in self._condtion[C.DISABLED]:
            self.sample_items[key].configure(state=state)

    def on_change_conf(self, item_name: str, values: THEME_DATA_TYPE) -> None:  # noqa: C901, PLR0912
        """Change the widget configuration.

        Args:
            item_name (str): Widget name.
            values (THEME_DATA_TYPE): Setting value.
        """
        if item_name == W.CTK:
            self.sample_items[item_name].configure(fg_color=values[S.FG_COLOR])
        elif item_name == W.TOPLEVEL:
            if (W.TOPLEVEL in self.sample_items
            and self.sample_items[W.TOPLEVEL].winfo_exists()
            ):
                self.sample_items[item_name].configure(fg_color=values[S.FG_COLOR])
        elif item_name == W.BUTTON:
            self.sample_items[item_name].configure(
                border_color=values[S.BORDER_COLOR],
                border_width=values[S.BORDER_WIDTH],
                corner_radius=values[S.CORNER_RADIUS],
                fg_color=values[S.FG_COLOR],
                hover_color=values[S.HOVER_COLOR],
                text_color=values[S.TEXT_COLOR],
                text_color_disabled=values[S.TEXT_COLOR_DISABLED],
            )
        elif item_name == W.RADIOBUTTON:
            self.sample_items[item_name].configure(
                border_color=values[S.BORDER_COLOR],
                border_width_checked=values[S.BORDER_WIDTH_CHECKED],
                border_width_unchecked=values[S.BORDER_WIDTH_UNCHECKED],
                corner_radius=values[S.CORNER_RADIUS],
                fg_color=values[S.FG_COLOR],
                hover_color=values[S.HOVER_COLOR],
                text_color=values[S.TEXT_COLOR],
                text_color_disabled=values[S.TEXT_COLOR_DISABLED],
            )
        elif item_name == W.SEGMENTEDBUTTON:
            self.sample_items[item_name].configure(
                border_width=values[S.BORDER_WIDTH],
                corner_radius=values[S.CORNER_RADIUS],
                fg_color=values[S.FG_COLOR],
                selected_color=values[S.SELECTED_COLOR],
                selected_hover_color=values[S.SELECTED_HOVER_COLOR],
                text_color=values[S.TEXT_COLOR],
                text_color_disabled=values[S.TEXT_COLOR_DISABLED],
                unselected_color=values[S.UNSELECTED_COLOR],
                unselected_hover_color=values[S.UNSELECTED_HOVER_COLOR],
            )
        elif item_name == W.ENTRY:
            self.sample_items[item_name].configure(
                border_color=values[S.BORDER_COLOR],
                border_width=values[S.BORDER_WIDTH],
                corner_radius=values[S.CORNER_RADIUS],
                fg_color=values[S.FG_COLOR],
                placeholder_text_color=values[S.PLACEHOLDER_TEXT_COLOR],
                text_color=values[S.TEXT_COLOR],
            )
        elif item_name == W.LABEL:
            self.sample_items[item_name].configure(
                corner_radius=values[S.CORNER_RADIUS],
                fg_color=values[S.FG_COLOR],
                text_color=values[S.TEXT_COLOR],
            )
        elif item_name == W.CHECKBOX:
            self.sample_items[item_name].configure(
                border_color=values[S.BORDER_COLOR],
                border_width=values[S.BORDER_WIDTH],
                checkmark_color=values[S.CHECKMARK_COLOR],
                corner_radius=values[S.CORNER_RADIUS],
                fg_color=values[S.FG_COLOR],
                hover_color=values[S.HOVER_COLOR],
                text_color=values[S.TEXT_COLOR],
                text_color_disabled=values[S.TEXT_COLOR_DISABLED],
            )
        elif item_name == W.SWITCH:
            self.sample_items[item_name].configure(
                border_width=values[S.BORDER_WIDTH],
                button_color=values[S.BUTTON_COLOR],
                button_hover_color=values[S.BUTTON_HOVER_COLOR],
                button_length=values[S.BUTTON_LENGTH],
                corner_radius=values[S.CORNER_RADIUS],
                fg_color=values[S.FG_COLOR],
                progress_color=values[S.PROGRESS_COLOR],
                text_color=values[S.TEXT_COLOR],
                text_color_disabled=values[S.TEXT_COLOR_DISABLED],
            )
        elif item_name == W.PROGRESSBAR:
            self.sample_items[item_name].configure(
                border_color=values[S.BORDER_COLOR],
                border_width=values[S.BORDER_WIDTH],
                corner_radius=values[S.CORNER_RADIUS],
                fg_color=values[S.FG_COLOR],
                progress_color=values[S.PROGRESS_COLOR],
            )
        elif item_name == W.SLIDER:
            self.sample_items[item_name].configure(
                border_width=values[S.BORDER_WIDTH],
                button_color=values[S.BUTTON_COLOR],
                button_corner_radius=values[S.BUTTON_CORNER_RADIUS],
                button_hover_color=values[S.BUTTON_HOVER_COLOR],
                button_length=values[S.BUTTON_LENGTH],
                corner_radius=values[S.CORNER_RADIUS],
                fg_color=values[S.FG_COLOR],
                progress_color=values[S.PROGRESS_COLOR],
            )
        elif item_name == W.OPTIONMENU:
            self.sample_items[item_name].configure(
                button_color=values[S.BUTTON_COLOR],
                button_hover_color=values[S.BUTTON_HOVER_COLOR],
                corner_radius=values[S.CORNER_RADIUS],
                fg_color=values[S.FG_COLOR],
                text_color=values[S.TEXT_COLOR],
                text_color_disabled=values[S.TEXT_COLOR_DISABLED],
            )
        elif item_name == W.COMBOBOX:
            self.sample_items[item_name].configure(
                border_color=values[S.BORDER_COLOR],
                border_width=values[S.BORDER_WIDTH],
                button_color=values[S.BUTTON_COLOR],
                button_hover_color=values[S.BUTTON_HOVER_COLOR],
                corner_radius=values[S.CORNER_RADIUS],
                fg_color=values[S.FG_COLOR],
                text_color=values[S.TEXT_COLOR],
                text_color_disabled=values[S.TEXT_COLOR_DISABLED],
            )
        elif item_name == W.TEXTBOX:
            self.sample_items[item_name].configure(
                border_color=values[S.BORDER_COLOR],
                border_width=values[S.BORDER_WIDTH],
                corner_radius=values[S.CORNER_RADIUS],
                fg_color=values[S.FG_COLOR],
                scrollbar_button_color=values[S.SCROLLBAR_BUTTON_COLOR],
                scrollbar_button_hover_color=values[S.SCROLLBAR_BUTTON_HOVER_COLOR],
                text_color=values[S.TEXT_COLOR],
            )
        elif item_name == W.DROPDOWNMENU:
            self.sample_items[item_name][W.OPTIONMENU].configure(
                fg_color=values[S.FG_COLOR],
                hover_color=values[S.HOVER_COLOR],
                text_color=values[S.TEXT_COLOR],
            )
            self.sample_items[item_name][W.COMBOBOX].configure(
                fg_color=values[S.FG_COLOR],
                hover_color=values[S.HOVER_COLOR],
                text_color=values[S.TEXT_COLOR],
            )
        elif item_name == W.FRAME:
            # [Attention]
            # When the parent's fg_color and its own fg_color are the same,
            # top_fg_color is set instead of fg_color inside CustomTkinter.
            self.sample_items[item_name].configure(
                border_color=values[S.BORDER_COLOR],
                border_width=values[S.BORDER_WIDTH],
                corner_radius=values[S.CORNER_RADIUS],
                fg_color=values[S.FG_COLOR],
                # top_fg_color=values['top_fg_color'],
            )
        elif item_name == W.SCROLLBAR:
            self.sample_items[item_name].configure(
                border_spacing=values[S.BORDER_SPACING],
                button_color=values[S.BUTTON_COLOR],
                button_hover_color=values[S.BUTTON_HOVER_COLOR],
                corner_radius=values[S.CORNER_RADIUS],
                fg_color=values[S.FG_COLOR],
            )
        elif item_name == W.SCROLLABLEFRAME:
            self.sample_items[item_name].configure(
                label_fg_color=values[S.LABEL_FG_COLOR],
            )
        elif item_name == W.FONT:
            os_name = platform.system() if platform.system() != 'Drawin' else 'macOS'
            font = ctk.CTkFont(
                family=values[os_name][S.FAMILY],
                size=values[os_name][S.SIZE],
                weight=values[os_name][S.WEIGHT],
            )
            for key, item in self.sample_items.items():
                if W.DROPDOWNMENU in key:
                    item[W.OPTIONMENU].configure(font=font)
                    item[W.COMBOBOX].configure(font=font)
                elif all(k not in key for k in self._condtion[C.FONT]):
                    item.configure(font=font)
