from flask import Blueprint, render_template
home_page = Blueprint("home", __name__, static_folder="static", template_folder="templates")
from api.api import Get_dog
import requests
BASE = "http://127.0.0.1:5000/api"
@home_page.route("/home")
@home_page.route("/")
def home():
    response = requests.get(BASE + f"/dog/get/") 
    dog_data = response.json()
    return render_template("index.html", dogs=dog_data)
