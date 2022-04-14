from flask import render_template, abort

from app import app, candidates
from utility.utils import find_candidate_by_uid, find_candidates_by_skill


@app.route('/')
def index() -> str:
    """
    Главная страница со списком всех кандидатов. Предоставляет информацию об имени, позиции и навыках.
    """
    return render_template("index.html", candidates=candidates)


@app.route('/candidates/<int:uid>')
def candidate_profile(uid: int) -> str:
    """
    Страница профиля кандидата.
    """
    try:
        candidate = find_candidate_by_uid(candidates, uid)
    except ValueError as e:  # Если нет кандидата с данным uid.
        print(e)
        abort(404)
    return render_template("candidate.html", candidate=candidate)


@app.route('/skills/<skill>')
def search_by_skill(skill: str) -> str:
    """
    Страница с информацией о тех кандидатах, у которых есть навык skill.
    """
    filtered_candidates = find_candidates_by_skill(candidates, skill)
    return render_template("search_by_skill.html", candidates=filtered_candidates, skill=skill)
