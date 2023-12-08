from flask import Blueprint, render_template
home = Blueprint("home", __name__, static_folder="static", template_folder="templates")

@home.route("/home")
@home.route("/")
def home():
    return render_template("index.html")
