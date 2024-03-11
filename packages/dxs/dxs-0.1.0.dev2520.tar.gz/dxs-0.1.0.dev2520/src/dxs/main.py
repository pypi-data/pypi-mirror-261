from typer import Typer, prompt, style, colors
import toml
from shutil import copy, copytree, ignore_patterns
from os import mkdir, listdir
from pathlib import Path
from rich import print

VERSION = "0.1.0"


def _copy_template(from_path: str, to_path: str, name_to_path: str, is_package: bool):
    struct = Path(__file__).parent / from_path

    to_path = to_path / name_to_path
    mkdir(to_path)

    patterns_to_ignore = ["__pycache__"]

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

    if is_package == "y":
        package = to_path / "src" / name_to_path
        mkdir(package)

        with open(f"{package}/main.py", "w"):
            pass
        with open(f"{package}/__init__.py", "w"):
            pass

    colors = [
        "bright_yellow",
        "dark_cyan",
        "gold1",
        "dodger_blue1",
        "deep_pink2",
        # "orange3",
    ]
    n_color = 0
    dir = ["src", "test"]

    print("\n[gold]> Initializing project: [/gold]")
    print(f"[{colors[3]}] : ./src [/{colors[3]}] created")
    print(f"[{colors[4]}] : ./test [/{colors[4]}] created")
    for file in listdir(struct):
        if file not in dir:
            print(f"[{colors[n_color]}] : {file} [/{colors[n_color]}] created")
            n_color += 1
    print("\n[blue]● It has finished correctly.[/blue]")


app = Typer(rich_markup_mode="rich")


@app.command("init", help="Create a new project!")
def init():
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
        f"Project License {style('(Apache)', fg=colors.GREEN, bold=True)}",
        default="MIT",
        show_default=False,
    )
    description = prompt(
        "Description",
        default=f"new project {name}",
        show_default=False,
    )
    author = prompt("Project Author")
    email = prompt("Email Author")
    python = prompt(
        f"requires-python {style('(>=3.8)', fg=colors.GREEN, bold=True)}",
        default=">=3.8",
        show_default=False,
    )
    package = prompt(
        f"Is a package (y/n) {style('(n)', fg=colors.GREEN, bold=True)}",
        default="n",
        show_default=False,
    )

    toml_dict = {
        "project": {
            "name": name,
            "version": version,
            "license": {"text": license},
            "description": description,
            "authors": [{"name": author, "email": email}],
            "dependencies": [],
            "requires-python": python,
            "readme": "README.md",
            "keywords": ["dxs"],
            "classifiers": [
                "Topic :: Software Development :: Build Tools",
                "Programming Language :: Python :: 3.8",
                "Programming Language :: Python :: 3.9",
                "Programming Language :: Python :: 3.10",
                "Programming Language :: Python :: 3.11",
                "Programming Language :: Python :: 3.12",
            ],
            "urls": {
                "Homepage": f"https://github.com/{author}/",
                "Repository": f"https://github.com/{author}/{name}",
                "Documentation": f"https://github.com/{author}/{name}/blob/main/README.md",
                "Changelog": f"https://github.com/{author}/{name}/blob/main/README.md",
            },
            "scripts": {"dxs": "dxs.main:app"},
        },
        "build-system": {
            "requires": ["pdm-backend"],
            "build-backend": "pdm.backend",
        },
        "tool": {
            "pdm": {
                "distribution": True,
                "build": {
                    "excludes": ["./**/.git"],
                    "package-dir": "src",
                    "includes": [f"src/{name}"],
                    "source-includes": ["LICENSE", "README.md"],
                },
            },
        },
    }
    _copy_template("templates", pwd, name, package)

    with open(f"{pwd}/{name}/pyproject.toml", "w") as file:
        toml.dump(toml_dict, file)

    print("[green]It has been successfully created![/green]")


@app.command("version", help="Package version")
def version():
    print(f"Flet-Easy, version [green]{VERSION}[/green]")


if __name__ == "__main__":
    app()
