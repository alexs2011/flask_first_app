from flask import Flask

import utils

app = Flask(__name__)

candidates = utils.load_data(r"./data/candidates.json")
