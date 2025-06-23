<!-- ============================================================
  Project Image
 ============================================================ -->
<div align=center>
  <img
    src='docs/image/demo.gif'
    alt='Project Image.'
    width=500
  />
</div>

<!-- ============================================================
  Overview
 ============================================================ -->
# :book:Overview

[![English](https://img.shields.io/badge/English-018EF5.svg?labelColor=d3d3d3&logo=readme)](./README.md)
[![Japanese](https://img.shields.io/badge/Japanese-018EF5.svg?labelColor=d3d3d3&logo=readme)](./README_JA.md)
[![license](https://img.shields.io/github/license/r-dev95/customtkinter-create-theme-app)](./LICENSE)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

[![Python](https://img.shields.io/badge/Python-3776AB.svg?labelColor=d3d3d3&logo=python)](https://github.com/python)
[![Sphinx](https://img.shields.io/badge/Sphinx-000000.svg?labelColor=d3d3d3&logo=sphinx&logoColor=000000)](https://github.com/sphinx-doc/sphinx)
[![Pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?labelColor=d3d3d3&logo=pytest)](https://github.com/pytest-dev/pytest)
[![Pydantic](https://img.shields.io/badge/Pydantic-ff0055.svg?labelColor=d3d3d3&logo=pydantic&logoColor=ff0055)](https://github.com/pydantic/pydantic)

This is a GUI app to create CustomTkinter theme files.

With this app, you can easily create your own theme files while checking the widget theme in real time.

> [!note]
> CustomTkinter allows you to use pre-prepared themes.
> You can also use your own themes by specifying the file path.
>
> ```python
> import customtkinter as ctk
> ctk.set_default_color_theme(color_string='blue') # blue, dark-blue, green
> ```

<!-- ============================================================
  Features
 ============================================================ -->
## :desktop_computer:Features

### Home page

<div align=center>
  <img
    src='docs/image/app_home.png'
    alt='App Home Page.'
    width=500
  />
</div>

|Item                     |Features                              |
| ---                     | ---                                  |
|Light/Dark toggle button |Light/dark mode toggle.               |
|Sidebar button (Home)    |Display the Home page.                |
|Select button            |Select the base theme file.           |
|Save button              |Save the file with the theme you set. |

### Setting page (Other than the Home page)

<div align=center>
  <img
    src='docs/image/app_no_home.png'
    alt='App Setting and Sample Page.'
    width=500
  />
</div>

|Item                                   |Features                                     |
| ---                                   | ---                                         |
|Sidebar buttons (Other than Home)      |Display the settings page of each widget.    |
|Each text area (center of screen)      |Set the widget theme.                        |
|Each widget (right side of the screen) |Display samples according to theme settings. |

※For color, the text area on the left is for light mode and the one on the right is for dark mode.

<!-- ============================================================
  Usage
 ============================================================ -->
## :keyboard:Usage

### Install

```bash
git clone https://github.com/r-dev95/customtkinter-create-theme-app.git
```

### Build virtual environment

You need to install `uv`.

If you don't have a python development environment yet, see [here](https://github.com/r-dev95/env-python).

```bash
cd customtkinter-create-theme-app/
uv sync
```

### Run

```bash
cd src
uv run python app.py
```

- Press the Select button on the Home page to select the base theme file.

  Depending on the theme file you select, a settings page for each widget will be generated.

- You set the theme on each widget's settings page.

  You can check the settings in real time on the sample page (right side of the screen) or in the app itself.

- Once you have finished the settings, press the Save button on the Home page to create the theme file.

> [!note]
>
> - The `CTk` setting is reflected in this app itself, not the sample page.
> - The settings of `DropdownMenu` are reflected in `CTkOptionMenu` and `CTkComboBox`.
> - To check the `CTkToplevel` settings, click the `Open Top Level Window` button on the sample page to display the window.
> - To check the `***_disabled` settings, press the `Disabled Sample` toggle button.
> - When instantiating a `CTkFrame`, if the parent's and its `fg_color` are the same, `top_fg_color` will be set instead of `fg_color` inside CustomTkinter.
>
>   Therefore, `top_fg_color` cannot be checked in this app, where theme changes are reflected in `.configure`.

<!-- ============================================================
  Structure
 ============================================================ -->
## :bookmark_tabs:Structure

<div align=center>
  <img
    src='docs/image/classes.png'
    alt='classes.'
  />
</div>

<!-- ============================================================
  License
 ============================================================ -->
## :key:License

This repository is licensed under the [MIT License](LICENSE).
