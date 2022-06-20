from application import app, db
from application.models import Todos
from flask import Flask, redirect, url_for, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField('Add Name')

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def index():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {first_name} {last_name}'

    return render_template('home.html', form=form, message=message)
   

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/firsttask')
def htmldone():
    todo=Todos.query.all()
    return render_template("tasks.html",todos=todo)










@app.route('/alltasks')
def done():
    todo=Todos.query.all()
    empstr = ""    
    for t in todo:
        empstr += f'{t.id} {t.task}  {t.completed} <br>'    
    return empstr



