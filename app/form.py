from flask_wtf import Form
from wtforms import TextField, SubmitField

#text displayed in the initial page that prompts user for locations
class prompt(Form):
    name = TextField("Please enter your name: ")
    phone= TextField("Enter your cell phone #: ")
    task= TextField("Task: ")
    importance= TextField("Important (1-5): ")
    date= TextField("Complete by: (mm/dd/yyyy)")
    time= TextField("Time: (HH:MM) ")
    submit = SubmitField("Text me")

