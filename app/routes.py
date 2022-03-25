from flask import render_template
from app import myobj, name, city_names


@myobj.route('/')
def home():
    return render_template("home.html", name=name, cities=city_names)
