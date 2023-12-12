from flask import Blueprint, render_template
auth = Blueprint("auth", __name__, static_folder="static", template_folder="templates")

@auth.route("/login")
def login():
    return render_template("index.html")
@auth.route("/register")
def register():
    return render_template("index.html")

@auth.route("/logout")
def logout():
    return render_template("index.html")
