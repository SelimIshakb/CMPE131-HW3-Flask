from flask import Flask
from config import Config

name = "Selim"
city_names = ["Istanbul", "Ankara", "Izmir", "Bursa"]
myobj = Flask(__name__)
myobj.config.from_mapping(SECRET_KEY="super secret key")

from app import routes
