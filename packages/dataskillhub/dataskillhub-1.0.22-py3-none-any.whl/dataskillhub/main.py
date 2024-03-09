from pathlib import Path

import click

from .export import write_exports
from .extract_consultants import get_cvs
from .init_src import copy_file, creer_dossier

BASE_PATH = "sources_exemple"
DESTINATION_PATH = "src"
OUTPUT_PATH = "src/outputs"


@click.group()
def main():
    pass

"""
@main.command()
@click.option("--destination", default=".", help="Where to init")
def init(destination="."):
    list_dossier = ["assets", "templates", "config", "consultants"]
    for dossier in list_dossier:
        creer_dossier(f"{destination}/{dossier}/")

    code_path = Path(__file__).parent

    copy_file(code_path / "assets", f"{destination}/assets", "logo_pied.png")
    copy_file(code_path / "assets", f"{destination}/assets", "Datalyo_logo_rvb.png")
    copy_file(code_path / "assets", f"{destination}/assets", "test.css")
    copy_file(code_path / "templates", f"{destination}/templates", "temp_cv.html")
    copy_file(code_path / "config", f"{destination}/config", "anonyme.json")
    print("fichiers prêt")
"""


@main.command()
def init():
    list_dossier = ["assets", "templates", "config", "consultants"]
    for dossier in list_dossier:
        creer_dossier(f"{DESTINATION_PATH}/{dossier}/")

    code_path = Path(__file__).parent

    copy_file(code_path / "assets", f"{DESTINATION_PATH}/assets", "logo_pied.png")
    copy_file(code_path / "assets", f"{DESTINATION_PATH}/assets", "Datalyo_logo_rvb.png")
    copy_file(code_path / "assets", f"{DESTINATION_PATH}/assets", "test.css")
    copy_file(code_path / "templates", f"{DESTINATION_PATH}/templates", "temp_cv.html")
    copy_file(code_path / "config", f"{DESTINATION_PATH}/config", "anonyme.json")
    print("fichiers prêt")


@main.group()
def consultant():
    pass


@consultant.command()
@click.argument("consultant")
def export(consultant):
    consultants_path = f"{DESTINATION_PATH}/consultants/"
    cvs = get_cvs(consultant, consultants_path)
    write_exports(cvs, OUTPUT_PATH, consultant)


@consultant.command()
def list():
    print("ok list")


@consultant.command()
@click.argument("consultant")
def new(consultant):
    print(f"new {consultant}")


@consultant.command()
@click.argument("consultant")
def check(consultant):
    print(f"check {consultant}")


if __name__ == "__main__":
    main()
