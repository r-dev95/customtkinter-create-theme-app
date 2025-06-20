"""This is the module that defines CustomTkinter Theme Setting App.
"""

import argparse
from logging import getLogger
from pathlib import Path
from typing import TYPE_CHECKING, Any

import customtkinter as ctk

from lib.common.decorator import process_time, save_params_log
from lib.common.file import load_yaml
from lib.common.log import SetLogging
from lib.common.types import THEME_DATA_TYPE, ParamLog, SideBarFrameName
from lib.common.types import EventName as E
from lib.common.types import ParamKey as K
from lib.components.base import EventBus
from lib.components.home import FIRST_PAGE_NAME, HomePage
from lib.components.sample import SamplePage
from lib.components.setting import SettingPage
from lib.components.sidebar import SideBar

if TYPE_CHECKING:
    from lib.components.base import BasePage

PARAM_LOG = ParamLog()
LOGGER = getLogger(PARAM_LOG.NAME)


class App(ctk.CTk):
    """Define the main App.
    """
    def __init__(self, params: dict[str, Any]) -> None:
        super().__init__()
        ctk.set_appearance_mode(mode_string=params[K.MODE])
        ctk.set_default_color_theme(color_string=params[K.THEME])

        self.title('CustomTkinter Theme Setting App')
        self.geometry('1200x650')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((1, 2), weight=1)

        self.event_bus = EventBus()

        self.sidebar = SideBar(master=self, event_bus=self.event_bus)
        self.sidebar.grid(row=0, column=0, sticky=ctk.NS)

        # [Attention]
        # Although it is not visible, it is also displayed behind the Home page.
        self.sample_page = SamplePage(master=self, event_bus=self.event_bus)
        self.sample_page.grid(row=0, column=2, sticky=ctk.NSEW)

        self.current_setting_page: BasePage = None
        self.setting_pages: dict[str, BasePage] = {
            FIRST_PAGE_NAME: HomePage(master=self, event_bus=self.event_bus),
        }

        self.event_bus.subscribe(event_name=E.SHOW_PAGE, callback=self.on_show_page)
        self.event_bus.subscribe(event_name=E.BUILD_PAGE, callback=self.on_build_page)

        self.event_bus.emit(
            event_name=E.ADD_BUTTON,
            frame_name=SideBarFrameName.HEADER,
            page_name=FIRST_PAGE_NAME,
        )
        self.event_bus.emit(event_name=E.SHOW_PAGE, page_name=FIRST_PAGE_NAME)

    def on_show_page(self, page_name: str) -> None:
        """Display the page that corresponds to the button in the sidebar.

        Args:
            page_name (str): Page name.
        """
        LOGGER.debug(f'{page_name=}')
        if self.current_setting_page is not None:
            self.current_setting_page.grid_forget()
        self.current_setting_page = self.setting_pages[page_name]
        if page_name != FIRST_PAGE_NAME:
            self.current_setting_page.grid(row=0, column=1, sticky=ctk.NSEW)
        else:
            self.current_setting_page.grid(
                row=0,
                column=1,
                columnspan=2,
                sticky=ctk.NSEW,
            )

    def on_build_page(self, data: THEME_DATA_TYPE) -> None:
        """Build sidebar buttons and settings page based on loaded theme data.

            *   Remove all sidebar buttons and settings pages if they have already been
                built.

        Args:
            data (THEME_DATA_TYPE): Theme data.
        """
        self.event_bus.emit(
            event_name=E.DEL_ALL_BUTTON,
            exclude_page_name=FIRST_PAGE_NAME,
        )
        for key in list(self.setting_pages):
            LOGGER.debug(f'{key=}')
            if key != FIRST_PAGE_NAME:
                self.setting_pages[key].destroy()
                del self.setting_pages[key]

        for key, val in data.items():
            LOGGER.debug(f'{key=}, {val=}')
            self.event_bus.emit(
                event_name=E.ADD_BUTTON,
                frame_name=SideBarFrameName.MAIN,
                page_name=key,
            )
            self.setting_pages[key] = SettingPage(
                master=self,
                event_bus=self.event_bus,
                page_name=key,
                values=val,
            )


@save_params_log(fname=f'log_params_{Path(__file__).stem}.yaml')
@process_time(print_func=LOGGER.info)
def main(params: dict[str, Any]) -> dict[str, Any]:
    """Main.

    This function is decorated by ``@save_params_log`` and ``@process_time``.

    Args:
        params (dict[str, Any]): parameters.

    Returns:
        dict[str, Any]: parameters.
    """
    app = App(params=params)
    app.mainloop()
    return params


def set_params() -> dict[str, Any]:
    """Sets the command line arguments and file parameters.

    *   Set only common parameters as command line arguments.
    *   Other necessary parameters are set in the file parameters.
    *   Use a yaml file. (:func:`lib.common.file.load_yaml`)

    Returns:
        dict[str, Any]: parameters.

    .. attention::

        Command line arguments are overridden by file parameters.
        This means that if you want to set everything using file parameters,
        you don't necessarily need to use command line arguments.
    """
    # set the command line arguments.
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        f'--{K.HANDLER}',
        default=[True, True], type=bool, nargs=2,
        help=(
            f'The log handler flag to use.\n'
            f'True: set handler, False: not set handler\n'
            f'ex) --{K.HANDLER} arg1 arg2 (arg1: stream handler, arg2: file handler)'
        ),
    )
    parser.add_argument(
        f'--{K.LEVEL}',
        default=[20, 20], type=int, nargs=2, choices=[10, 20, 30, 40, 50],
        help=(
            f'The log level.\n'
            f'DEBUG: 10, INFO: 20, WARNING: 30, ERROR: 40, CRITICAL: 50\n'
            f'ex) --{K.LEVEL} arg1 arg2 (arg1: stream handler, arg2: file handler)'
        ),
    )
    parser.add_argument(
        f'--{K.PARAM}',
        default='param/param.yaml', type=str,
        help=('The parameter file path.'),
    )
    parser.add_argument(
        f'--{K.RESULT}',
        default='result', type=str,
        help=('The directory path to save the results.'),
    )
    parser.add_argument(
        f'--{K.MODE}',
        default='system', type=str, choices=['system', 'light', 'dark'],
        help=('The light/dark mode flag.'),
    )
    parser.add_argument(
        f'--{K.THEME}',
        default='blue', type=str,
        help=(
            'The CustomTkinter theme color.\n'
            'The choice is blue / dark-blue / green or json file path.'
        ),
    )

    params = vars(parser.parse_args())

    # set the file parameters.
    if params.get(K.PARAM):
        fpath = Path(params[K.PARAM])
        if fpath.is_file():
            params.update(load_yaml(fpath=fpath))

    return params


if __name__ == '__main__':
    # set the parameters.
    params = set_params()
    # set the logging configuration.
    PARAM_LOG.HANDLER[PARAM_LOG.SH] = params[K.HANDLER][0]
    PARAM_LOG.HANDLER[PARAM_LOG.FH] = params[K.HANDLER][1]
    PARAM_LOG.LEVEL[PARAM_LOG.SH] = params[K.LEVEL][0]
    PARAM_LOG.LEVEL[PARAM_LOG.FH] = params[K.LEVEL][1]
    SetLogging(logger=LOGGER, param=PARAM_LOG)

    if params.get(K.RESULT):
        Path(params[K.RESULT]).mkdir(parents=True, exist_ok=True)

    main(params=params)
