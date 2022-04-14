from flask import render_template

from app import app, candidates


@app.route('/')
def index() -> str:
    """
    Главная страница со списком всех кандидатов. Предоставляет информацию об имени, позиции и навыках.
    """
    return render_template("index.html", candidates=candidates)
