from flask import render_template, abort

from app import app, candidates
from utility.utils import find_candidate_by_uid


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
    except ValueError as e:
        print(e)
        abort(404)
    return render_template("candidate.html", candidate=candidate)
