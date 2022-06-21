from application import app
from flask import Flask, render_template, request
from application import db

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)


app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'



















