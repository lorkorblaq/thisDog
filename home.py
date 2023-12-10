from flask import Blueprint, render_template
home_page = Blueprint("home", __name__, static_folder="static", template_folder="templates")

@home_page.route("/home")
@home_page.route("/")
def home():
    return render_template("index.html")