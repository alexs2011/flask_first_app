import json


def load_data(filename: str) -> list[dict]:
    """
    Загружает данные из файла формата JSON.
    """
    with open(filename, 'r', encoding='utf-8') as f_in:
        return json.load(f_in)


def find_candidate_by_uid(candidates: list[dict], uid: int) -> dict:
    """
    Поиск кандидата по uid.
    """
    for candidate in candidates:
        if candidate.get("id") == uid:
            return candidate
    raise ValueError(f"ValueError: Кандидат с uid={uid} не найден.")


def find_candidates_by_skill(candidates: list[dict], skill: str) -> list[dict]:
    """
    Поиск всех кандидатов, у которых есть навык skill.
    """
    res = []
    for candidate in candidates:
        skills = candidate.get("skills").lower().split(", ")
        if skill.lower() in skills:
            res.append(candidate)
    return res
