import json
from pathlib import Path


class DataReader:

    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / "test_data"

    @classmethod
    def load_json(cls, filename):

        file_path = cls.DATA_DIR / filename

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
