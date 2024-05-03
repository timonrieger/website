from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length, NumberRange, ValidationError
from wtforms import StringField, SelectField, IntegerField, SelectMultipleField, SubmitField, TextAreaField, DateField
import requests

NPOINT = "https://api.npoint.io/9e625c836edf8e4047a8"

STRING_FIELD_STYLE = "width: 40%; height: 33px; margin: auto; display: block"
TEXT_AREA_STYLE = "width: 40%; height: 100px; margin: auto; display: block"
SELECT_MULTIPLE_STYLE = "width: 40%; height: 200px; margin: auto; display: block"
SUBMIT_STYLE = "margin-bottom: 10px"

class ValidateMaxNightsGreaterThanMin:
    def __init__(self, message=None):
        if not message:
            message = 'Maximum nights must be greater than minimum nights.'
        self.message = message

    def __call__(self, form, field):
        min_nights = form.min_nights.data
        max_nights = field.data
        if max_nights <= min_nights:
            raise ValidationError(self.message)


class AirNomadSocietyForm(FlaskForm):
    departure_choices = [f"{city['city']} | {city['code']}" for city in requests.get(url=NPOINT).json()['cities']]
    currency_choices = requests.get(url=NPOINT).json()["currencies"]
    country_choices = [country["country"] for country in requests.get(url=NPOINT).json()["countries"]]

    username = StringField(label="Username", validators=[DataRequired(), Length(min=3, max=20, message="Set a username within 3 - 8 characters.")], render_kw={"style": f"{STRING_FIELD_STYLE}"})
    email = StringField(label="Email", validators=[DataRequired(), Email()], render_kw={"style": f"{STRING_FIELD_STYLE}"})
    departure_city = SelectField(label="Departure City", choices=departure_choices, validators=[DataRequired()], render_kw={"style": f"{STRING_FIELD_STYLE}"})
    currency = SelectField(label="Currency", choices=currency_choices, validators=[DataRequired()], render_kw={"style": f"{STRING_FIELD_STYLE}"})
    min_nights = IntegerField(label="Minimum Nights", validators=[DataRequired(), NumberRange(min=1, message="Set to 1 or above.")], render_kw={"style": f"{STRING_FIELD_STYLE}"})
    max_nights = IntegerField(label="Maximum Nights", validators=[DataRequired(), NumberRange(max=180, message="Set to 180 or lower."), ValidateMaxNightsGreaterThanMin()], render_kw={"style": f"{STRING_FIELD_STYLE}"})
    favorite_countries = SelectMultipleField(label="Favorite destinations", choices=country_choices, validators=[DataRequired()], render_kw={"style": f"{SELECT_MULTIPLE_STYLE}; f{SUBMIT_STYLE}"})
    join = SubmitField(label="Join Air Nomad Society")
    update = SubmitField(label="Update Preferences", render_kw={"style": "margin: 10px"})

class ContactForm(FlaskForm):
    name = StringField(label="Name", render_kw={"style": f"{STRING_FIELD_STYLE}"}, validators=[DataRequired()])
    email = StringField(label="Email", render_kw={"style": f"{STRING_FIELD_STYLE}"}, validators=[DataRequired(), Email()])
    message = TextAreaField(label="Message", render_kw={"style": f"{STRING_FIELD_STYLE}; height: 150px; f{SUBMIT_STYLE}"}, validators=[DataRequired()])
    submit = SubmitField(label="Send")

class NewsletterForm(FlaskForm):
    email = StringField(label="Email", render_kw={"style": f"{STRING_FIELD_STYLE}; f{SUBMIT_STYLE}"}, validators=[DataRequired(), Email()])
    submit = SubmitField(label="Stay updated")

class FlashbackPlaylistsForm(FlaskForm):
    date_input = DateField(label="Date", render_kw={"style": f"{STRING_FIELD_STYLE}"}, validators=[DataRequired()])
    title = StringField(label="Playlist Title", render_kw={"style": f"{STRING_FIELD_STYLE}"}, validators=[DataRequired()])
    description = TextAreaField(label="Playlist Description", render_kw={"style": f"{TEXT_AREA_STYLE}; {SUBMIT_STYLE}"}, validators=[DataRequired(), Length(max=250, message="Maximum 250 characters.")])
    submit = SubmitField(label="Generate Playlist", render_kw={"id": "generateBtn"})