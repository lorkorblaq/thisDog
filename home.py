from flask import Blueprint, render_template
home_page = Blueprint("home", __name__, static_folder="static", template_folder="templates")
from api.api import Get_dog

@home_page.route("/home")
@home_page.route("/")
def home():
    dog_data=Get_dog()
    dog_data=dog_data.get()
    print(dog_data)
    return render_template("index.html", dogs=dog_data)
