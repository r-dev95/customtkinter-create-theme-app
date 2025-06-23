<!-- ============================================================ -->
<!-- Project Image -->
<!-- ============================================================ -->
<div align=center>
  <img
    src='docs/image/demo.gif'
    alt='Project Image.'
    width=500
  />
</div>

<!-- ============================================================ -->
<!-- Overview -->
<!-- ============================================================ -->
# Overview

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

CustomTkinterのテーマファイルを作成するGUIアプリです。

本アプリでは、ウィジェットのテーマをリアルタイムに確認しながら、テーマファイルを簡単に自作できます。

> [!note]
> CustomTkinterでは、予め用意されたテーマを使用できます。
> またファイルパスを指定することで、自作テーマも使用できます。
>
> ```python
> import customtkinter as ctk
> ctk.set_default_color_theme(color_string='blue') # blue, dark-blue, green
> ```

<!-- ============================================================ -->
<!-- Features -->
<!-- ============================================================ -->
## Features

### Home page

<div align=center>
  <img
    src='docs/image/app_home.png'
    alt='App Home Page.'
    width=500
  />
</div>

|項目                    |機能                            |
| ---                    | ---                            |
|Light/Darkトグルボタン  |ライト/ダークモードの切り替え。 |
|サイドバーボタン (Home) |Homeページの表示。              |
|選択ボタン              |ベースのテーマファイルの選択。  |
|保存ボタン              |設定したテーマのファイル保存。  |

### Setting page (Other than the Home page)

<div align=center>
  <img
    src='docs/image/app_no_home.png'
    alt='App Setting and Sample Page.'
    width=500
  />
</div>

|項目                        |機能                               |
| ---                        | ---                               |
|サイドバーボタン (Home以外) |各ウィジェットの設定ページの表示。 |
|各テキストエリア (画面中央) |ウィジェットテーマの設定。         |
|各ウィジェット (画面右)     |テーマ設定に応じたサンプルの表示。 |

※カラーの場合、左のテキストエリアがライトモード用、右がダークモード用です。

<!-- ============================================================ -->
<!-- Usage -->
<!-- ============================================================ -->
## Usage

### Install

```bash
git clone https://github.com/r-dev95/customtkinter-create-theme-app.git
```

### Build virtual environment

`uv`がインストールされていることが前提です。

pythonの開発環境がまだ整っていない方は、[こちら](https://github.com/r-dev95/env-python)。

```bash
cd customtkinter-create-theme-app/
uv sync
```

### Run

```bash
cd src
uv run python app.py
```

- Homeページの選択ボタンを押して、ベースとなるテーマファイルを選択します。

  選択したテーマファイルに応じて、各ウィジェットの設定ページが生成されます。

- 各ウィジェットの設定ページで好みのテーマ設定を行います。

  サンプルページ(画面右)または本アプリ自体に、設定はリアルタイムに反映され確認ができます。

- 設定が終わったら、Homeページの保存ボタンを押して、テーマファイルを作成します。

> [!note]
>
> - `CTk`の設定は、サンプルページではなく本アプリ自体に反映されます。
> - `DropdownMenu`の設定は、`CTkOptionMenu`と`CTkComboBox`に反映されます。
> - `CTkToplevel`の設定は、サンプルページの`Open Top Level Window`ボタンを押して、ウィンドウを表示させて確認してください。
> - `***_disabled`の設定は、`Disabled Sample`トグルボタンを押して確認してください。
> - `CTkFrame`をインスタンス化する際、親と自身の`fg_color`が同じ場合、CustomTkinter内部で`fg_color`の代わりに`top_fg_color`が設定される。
>
>   そのため`top_fg_color`は、テーマ変更を`.configure`で反映させる本アプリでは、確認できません。

<!-- ============================================================ -->
<!-- Structure -->
<!-- ============================================================ -->
## :bookmark_tabs:Structure

<div align=center>
  <img
    src='docs/image/classes.png'
    alt='classes.'
  />
</div>

<!-- ============================================================ -->
<!-- License -->
<!-- ============================================================ -->
## License

本リポジトリは、[MIT License](LICENSE)に基づいてライセンスされています。
