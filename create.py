from application import db
from application.models import Todos

db.drop_all()
db.create_all()
sample_todo=Todos(
    task="Sample todo",
    completed=False
)
second_todo=Todos(
    task="do homework for christian", 
    completed=False)
third_todo=Todos(task="beat the fuck out of him", completed=True)

db.session.add(sample_todo)
db.session.add(second_todo)
db.session.add(third_todo)
db.session.commit()