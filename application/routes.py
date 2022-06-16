from application import app, db
from application.models import ToDos




@app.route('/')
def index():
    todo=ToDos.query.first()
    return f'{todo.task}+{todo.completed}'

@app.route('/done')
def done():
    return "Task completed"