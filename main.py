import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Photos(db.Model):
    __tablename__ = "Photos"
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    photo_name = db.Column(db.String(25), nullable=False)
    likes_number = db.Column(db.Integer(25), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    hashtags = db.Column(db.String(25), nullable=False)
    effect = db.Column(db.String(25), nullable=False)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
