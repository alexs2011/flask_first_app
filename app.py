from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route('/')
def main_page() -> str:
    """
    Главная страница со списком всех кандидатов. Предоставляет информацию об имени, позиции и навыках.
    """
    return render_template("main_page.html", candidates=candidates)


if __name__ == "__main__":
    candidates = utils.load_data(r"./data/candidates.json")

    app.run(debug=True)
