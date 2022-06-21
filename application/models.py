from application import db




class Todos(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    task=db.Column(db.String(30))
    completed=db.Column(db.Boolean, default=False)

class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(30))
    last_name=db.Column(db.String(30))