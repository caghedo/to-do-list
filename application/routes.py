from application import app, db
from application.models import Todos
from flask import redirect, url_for, render_template




@app.route('/')
def index():
    todo=Todos.query.first()
    return f'{todo.task}{todo.completed}'

@app.route('/alltasks')
def done():
    todo=Todos.query.all()
    empstr = ""    
    for t in todo:
        empstr += f'{t.id} {t.task}  {t.completed} <br>'    
    return empstr


@app.route('/firsttask')
def htmldone():
    todo=Todos.query.all()
    return render_template("about.html",todos=todo)
