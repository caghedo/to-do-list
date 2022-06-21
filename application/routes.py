from application import app, db
from application.models import Todos,Users
from flask import Flask, redirect, url_for, render_template, request
from application.forms import BasicForm,UpdateForm,DeleteForm




app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def index():
    message = ""
    form = BasicForm()
    
    firstname=form.first_name.data
    lastname=form.last_name.data
    
    if request.method == 'POST':
        if form.validate_on_submit():
            firstname=form.first_name.data
            lastname=form.last_name.data
    
            if len(firstname) == 0 or len(lastname) == 0:
                message = "Please supply both first and last name"
            else:
                message = f'Thank you, {firstname} {lastname}'
            
            user1=Users(  
            first_name = form.first_name.data,
            last_name = form.last_name.data)

            db.session.add(user1)
            db.session.commit()
    firstname=form.first_name.data
    lastname=form.last_name.data
    

    
    return render_template('home.html', form=form, message=message)

@app.route('/users')
def users():
    user=Users.query.all()
    return render_template('users.html',user=user)

@app.route('/update', methods=['GET','POST'])
def update():
    form=UpdateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user=Users.query.get(form.id.data)
            user.first_name=form.first_name.data
            user.last_name=form.last_name.data
            db.session.commit()
    return render_template('update.html',form=form)

    
    
@app.route('/delete',methods=['GET','POST'])
def delete():
    form=DeleteForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user=Users.query.get(form.id.data)
            user.first_name=""
            user.last_name=""
            db.session.commit()
    return render_template('delete.html',form=form)
   

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



