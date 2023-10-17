from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField

class StudentForm(FlaskForm):
    id = StringField('Student ID')
    firstName = StringField('First Name')
    lastName = StringField('Last Name')
    course = StringField('Course')
    year = IntegerField('Year')  # IntegerField for numeric input
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')])  # SelectField for dropdown input
    submit = SubmitField('Submit')  # Submit button field