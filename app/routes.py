from flask import render_template, flash
from app import myobj
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

name = "Selim"
city_names = ["Istanbul", "Ankara", "Izmir", "Bursa"]


@myobj.route("/", methods=["GET", "POST"])
def home():
    form = CityForm()
    if form.validate_on_submit():
        flash(form.new_city.data)
    return render_template("home.html", name=name, cities=city_names, form=form)


class CityForm(FlaskForm):
    new_city = StringField("City Name", validators=[DataRequired()])
    submit = SubmitField()
