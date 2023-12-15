from flask import Blueprint, render_template, request
import requests


BASE = "http://127.0.0.1:5000/api"
views = Blueprint("views", __name__, static_folder="static", template_folder="templates")

@views.route("/",  strict_slashes=False)
def home():
    response = requests.get(BASE + f"/dogs/") 
    dog_data = response.json()
    return render_template("index.html", dogs=dog_data)
@views.route("/bids",  strict_slashes=False)
def bids():
    response = requests.get(BASE + f"/bids/") 
    bids_data = response.json()
    return render_template("bids.html", bids=bids_data)