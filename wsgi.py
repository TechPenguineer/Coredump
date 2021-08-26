from flask import *

app = Flask(__name__)

@app.route("/usr/new")
def index():
    return "Hello World"

