from flask_wtf import Form
from wtforms import TextField, SubmitField

#text displayed in the initial page that prompts user for locations
class prompt(Form):
    query = TextField("Please enter your phone number")
    submit = SubmitField("Text me")