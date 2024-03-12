from pathlib import Path


DESTINATION_PATH = "src"


def get_consultants():
    consultants_path = f"{DESTINATION_PATH}/consultants/"
    path = Path(consultants_path)
    for i in path.iterdir():
        print(i.name)


def add_consultant(consultant: str):
    consultants_path = f"{DESTINATION_PATH}/consultants/"
    folder_path = Path(f"{consultants_path}/{consultant}")
    folder_path.mkdir(parents=True, exist_ok=True)
