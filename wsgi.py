from flask import *

app = Flask(__name__)

@app.route("/usr/new")
def index():
    
    return render_template("register.html")

