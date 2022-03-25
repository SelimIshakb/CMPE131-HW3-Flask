from flask import Flask, render_template

myobj = Flask(__name__)

name = "Selim"
city_names = ["Istanbul", "Ankara", "Izmir", "Bursa"]


@myobj.route('/')
def home():
    return render_template("home.html", name=name, cities=city_names)

