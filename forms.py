from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, TextAreaField, validators
# from wtforms.validators import InputRequired, AnyOf, URL

# Form for new pet creation.
class NewPetForm(FlaskForm):

    valid_sp = ['cat', 'dog', 'porcupine']

    name = StringField("pet name", validators = [validators.InputRequired()])
    species = SelectField("species", choices = [(sp,sp) for sp in valid_sp], validators = [validators.InputRequired(), validators.AnyOf(valid_sp)])
    photo_url = StringField("photo URL", validators = [validators.URL(message = 'Invalid URL')])
    age = IntegerField(validators = [validators.NumberRange(min = 0, max = 30)])
    notes = TextAreaField("notes")

 # Form for editing pet on page.  
class EditPetForm(FlaskForm):

    photo_url = StringField("photo URL", validators = [validators.URL(message = 'Invalid URL')])
    notes = TextAreaField("notes")
    available = BooleanField()
   