import os
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify


base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Photos(db.Model):
    __tablename__ = "Photos"
    id = db.Column(db.Integer, nullable=False, unique=True,
                   primary_key=True, autoincrement=True)
    photo_name = db.Column(db.String(25), nullable=False)
    likes_number = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    hashtags = db.Column(db.String(25), nullable=False)
    effect = db.Column(db.String(25), nullable=False)

    def __init__(self, photo_name, description, hashtags, effect):
        self.photo_name = photo_name
        self.likes_number = 0
        self.description = description
        self.hashtags = hashtags
        self.effect = effect


class Comments(db.Model):
    __tablename__ = "Comments"
    id = db.Column(db.Integer, nullable=False, unique=True,
                   primary_key=True, autoincrement=True)
    photo_src = db.Column(db.String(30), nullable=False)
    comment_text = db.Column(db.Text(), nullable=False)

    def __init__(self, src, text):
        self.photo_src = src
        self.comment_text = text


@app.route("/api/get/data", methods=['GET'])
def get_data():
    user = {"name": "Pol", "password": "123"}
    return jsonify(user)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/upload/photo", methods=['POST'])
def upload_photo():
    file = request.files['file']
    lastRow = db.session.query(Photos).order_by(Photos.id.desc()).first()
    fileName = str(lastRow.id + 1)
    nameParts = file.filename.split('.')
    fileNameExtension = nameParts[len(nameParts) - 1]
    fileName += "." + fileNameExtension
    file.save(os.path.join("static", "img", "photos", fileName))
    description = request.form['description']
    hashtags = request.form['hashtags']
    effect = request.form['effect'] + '(' + request.form['effectLevel'] + "%)"
    row = Photos(fileName, description, hashtags, effect)
    db.session.add(row)
    db.session.commit()
    return redirect('/')


@app.route("/api/get/photos/all", methods=['GET'])
def get_photos():
    photos = Photos.query.all()
    photos_list = list()
    for photo in photos:
        photo_src = "../static/img/photos/" + photo.photo_name
        comments = db.session.query(Comments).filter_by(
            photo_src=photo_src).count()
        photo_dict = {"src": photo_src,
                      "likes": photo.likes_number,
                      "effect": photo.effect,
                      "commentsNumber": comments}
        photos_list.append(photo_dict)
    return jsonify(photos_list)


@app.route("/api/get/photo/data", methods=['POST'])
def getPhotoDetails():
    imageSrcParts = request.form['src'].split('/')
    imageName = imageSrcParts[len(imageSrcParts) - 1]
    image = Photos.query.filter_by(photo_name=imageName).first()
    image_comments = Comments.query.filter_by(photo_src=imageName).all()
    comments = []
    for comment in image_comments:
        comments.append(comment.comment_text)
    image_data = {
        "src": request.form['src'],
        "likes": image.likes_number,
        "effect": image.effect,
        "description": image.description,
        "comments": comments,
        "commentsNumber": len(comments)
    }
    return jsonify(image_data)


if __name__ == "__main__":
    app.run()
