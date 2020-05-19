from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets for adoption."""
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(require_tld=True, message=None)])
    age = IntegerField("Age", validators= [NumberRange(min=0, max=30, message=None)])
    notes = TextAreaField ("Notes")




