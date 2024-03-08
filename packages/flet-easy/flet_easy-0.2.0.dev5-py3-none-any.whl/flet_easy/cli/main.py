from rich import print
from typer import Typer, prompt, style, colors, confirm
from pathlib import Path
from pytoml import dump
from shutil import copy, copytree, ignore_patterns
from os import mkdir, listdir

VERSION = "0.1.2"


def _copy_template(from_path: str, to_path: str, manifest: bool):
    struct = Path(__file__).parent / from_path

    mkdir(to_path)

    patterns_to_ignore = [
        "__pycache__",
        "index.html",
        "manifest.json",
        "icons",
        "favicon.png",
    ]

    if manifest:
        patterns_to_ignore = patterns_to_ignore[:1]

    for item in struct.iterdir():
        try:
            if item.is_file():
                copy(item, to_path)
            elif item.is_dir():
                copytree(
                    item,
                    to_path / item.name,
                    ignore=ignore_patterns(*patterns_to_ignore),
                )
        except Exception as e:
            print(e)

    colors = [
        "bright_yellow",
        "dark_cyan",
        "gold1",
        "dodger_blue1",
        "deep_pink2",
        "orange3",
    ]
    n_color = 0

    not_files = ["__pycache__", "main.py", "README.md", ".gitignore"]

    print("\n[gold]> Initializing project: [/gold]")
    for folder in listdir(struct):
        if folder not in not_files:
            print(f"[{colors[n_color]}] : {folder} [/{colors[n_color]}] created")
            n_color += 1
    print("[light_sky_blue3] : main.py [/light_sky_blue3] created")
    if manifest:
        print(
            "\n[blue]● It has ended correctly. Remember to customize manifest.json and the icons in the assets folder :)[/blue]"
        )
    else:
        print("\n[blue]● It has finished correctly.[/blue]")


app = Typer(rich_markup_mode="rich", options_metavar="[aea]", rich_help_panel='ok')


@app.command("init", help="Create a new project!")
def init():
    toml_dict = {"project": {}}
    pwd = Path.cwd()

    name = prompt(
        f"Projet Name {style(f'({pwd.name})', fg=colors.GREEN, bold=True)}",
        default=pwd.name,
        show_default=False,
    )
    version = prompt(
        f"Project Version {style('(0.1.0)', fg=colors.GREEN, bold=True)}",
        default="0.1.0",
        show_default=False,
    )
    license = prompt(
        f"Project License {style('(MIT)', fg=colors.GREEN, bold=True)}",
        default="MIT",
        show_default=False,
    )
    author = prompt("Project Author")
    email = prompt("Email Author")
    manifest = confirm(
        f"Requires creation of manifest.json {style('(Web-PWA)', fg=colors.GREEN, bold=True)}",
    )

    toml_dict["project"]["name"] = name
    toml_dict["project"]["version"] = version
    toml_dict["project"]["license"] = license
    toml_dict["project"]["authors"] = [{"name": author, "email": email}]
    toml_dict["project"]["dependencies"] = ["flet-easy"]

    _copy_template("templates", pwd / name, manifest)

    with open(f"{pwd}/{name}/pyproject.toml", "w") as file:
        dump(toml_dict, file)


@app.command("version", help="Package version")
def version():
    print(f"Flet-Easy, version [green]{VERSION}[/green]")


if __name__ == "__main__":
    app()
