import json


def load_data(filename: str) -> list[dict]:
    """
    Загружает данные их файла формата JSON.
    """
    with open(filename, 'r', encoding='utf-8') as f_in:
        return json.load(f_in)


def find_candidate_by_uid(candidates: list[dict], uid: int) -> dict:
    for candidate in candidates:
        if candidate.get("id") == uid:
            return candidate
    raise ValueError(f"ValueError: Кандидат с uid={uid} не найден.")
