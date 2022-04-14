from flask import render_template

from app import app, candidates
from utility.utils import find_candidate_by_uid


@app.route('/')
def index() -> str:
    """
    Главная страница со списком всех кандидатов. Предоставляет информацию об имени, позиции и навыках.
    """
    return render_template("index.html", candidates=candidates)


@app.route('/candidates/<int:uid>')
def get_candidate_by_uid(uid: int) -> str:
    """
    Страница профиля кандидата.
    """
    candidate = find_candidate_by_uid(candidates, uid)
    return render_template("candidate.html", candidate=candidate)
