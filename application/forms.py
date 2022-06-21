from flask_wtf import FlaskForm
from application import app
from wtforms import IntegerField, StringField, SubmitField

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField('Add Name')

class UpdateForm(FlaskForm):
    id= IntegerField('Type ID here')
    first_name = StringField('Type your new first name here')
    last_name = StringField('Type your new last name here')
    submit = SubmitField('Change Name')

class DeleteForm(FlaskForm):
    id=IntegerField("Type ID here")
    submit=SubmitField("Delete name")