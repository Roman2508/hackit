import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, 'data.sqlite')}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = SQLAlchemy(app)


class Countries(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    continent = db.Column(db.String(25), nullable=False)
    photo_url = db.Column(db.String(), nullable=False)
    flag_url = db.Column(db.String(), nullable=False)

    def __init__(self, name, continent, photo_url, flag_url):
        self.name = name
        self.continent = continent
        self.photo_url = photo_url
        self.flag_url = flag_url


class Tours(db.Model):
    __tablename__ = 'tours'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    country = db.Column(db.String(25), nullable=False)
    city = db.Column(db.String(25), nullable=False)
    nights = db.Column(db.Integer, nullable=False)
    room_type = db.Column(db.String(25), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    departure = db.Column(db.String(10), nullable=False)
    arrival = db.Column(db.String(10), nullable=False)

    def __init__(self, name, country, city, nights, room_type, price, departure, arrival):
        self.name = name
        self.country = country
        self.city = city
        self.nights = nights
        self.room_type = room_type
        self.price = price
        self.departure = departure
        self.arrival = arrival


class Applications(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, name, phone, email, message):
        self.name = name
        self.phone = phone
        self.email = email
        self.message = message


@app.route('/', methods=["GET"])
def show_home_page():
    countries = Countries.query.all()
    tours = Tours.query.all()
    return render_template('index.html', is_home=True, countries=countries, tours=tours)


@app.route('/tour-details/<id>', methods=["GET"])
def show_tour_details(id):
    tour_details = Tours.query.filter_by(id=id)
    return jsonify(tour_details)
    

@app.route('/admin', methods=["GET"])
def show_admin_page():
    countries = Countries.query.all()
    tours = Tours.query.all()
    return render_template('admin.html', countries=countries, tours=tours)


@app.route('/create-country', methods=["POST"])
def create_country():
    name = request.form['name']
    continent = request.form['continent']
    photo_url = request.form['photo_url']
    flag_url = request.form['flag_url']
    row = Countries(name, continent, photo_url, flag_url)
    db.session.add(row)
    db.session.commit()
    return render_template('admin.html')


@app.route('/create-tour', methods=["POST"])
def create_tour():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    nights = request.form['nights']
    room_type = request.form['room_type']
    price = request.form['price']
    departure = request.form['departure']
    arrival = request.form['arrival']
    row = Tours(name, country, city, nights,
                room_type, price, departure, arrival)
    db.session.add(row)
    db.session.commit()
    return render_template('admin.html')


if __name__ == '__main__':
    app.run()
