from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)
class toDo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    task=db.Colummn(db.String(30))
    completed=db.Colummn(db.Boolean, default=False)



from application import routes









if __name__=="__main__":
    app.run(debug=True, hos='0.0.0.0', port=5000)