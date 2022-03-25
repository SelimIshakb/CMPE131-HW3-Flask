from flask import render_template
from app import myobj, name, city_names
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


@myobj.route('/')
def home():
    form = CityForm()
    return render_template("home.html", name=name, cities=city_names, form=form)


class CityForm(FlaskForm):
    new_city = StringField("City Name", validators=[DataRequired()])
    submit = SubmitField()
