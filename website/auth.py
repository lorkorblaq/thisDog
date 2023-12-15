from flask import Blueprint, render_template
from werkzeug.security import generate_password_hash, check_password_hash
auth = Blueprint("auth", __name__, static_folder="static", template_folder="templates")

@auth.route("/login")
def login():
    return render_template("login.html")
@auth.route("/register")
def register():
    return render_template("index.html")

@auth.route("/logout")
def logout():
    return render_template("index.html")
