import json
from pathlib import Path

TESTDATA_DIR = Path(__file__).resolve().parent.parent / "testdata"


def load_json(file_name):
    with open(TESTDATA_DIR / file_name, encoding="utf-8") as file:
        return json.load(file)
