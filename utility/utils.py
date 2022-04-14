import json


def load_data(filename: str) -> list[dict]:
    with open(filename, 'r', encoding='utf-8') as f_in:
        return json.load(f_in)