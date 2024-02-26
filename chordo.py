from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    

@app.route('/', methods = ['post', 'get'])
def index():
    return render_template('index.html')

@app.route("/calculate")
def calculate():
    return "LU IS SUPER GAY CAT VIBES MAN"


if __name__ == "__main__":
    app.run(debug=True)
