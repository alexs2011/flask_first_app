from flask import Flask

import utility.utils as utils

app = Flask(__name__)

candidates = utils.load_data(r"./data/candidates.json")
