from flask import Flask

import utility.utils as utils

app = Flask(__name__)

filename = r"./data/candidates.json"
candidates = utils.load_data(filename)
