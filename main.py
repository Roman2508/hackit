import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, "data.sqlite")}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.app_context().push()

db = SQLAlchemy(app)


@app.context_processor
def inject_tours():
    return dict(all_tours=Tours.query.all())


class Countries(db.Model):
    __tablename__ = "countries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    continent = db.Column(db.String(30), nullable=False)
    photo_url = db.Column(db.String(), nullable=False)
    flag_url = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, continent, photo_url, flag_url, description):
        self.name = name
        self.continent = continent
        self.photo_url = photo_url
        self.flag_url = flag_url
        self.description = description


class Tours(db.Model):
    __tablename__ = 'tours'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    departure = db.Column(db.String(30), nullable=False)
    nights = db.Column(db.Integer, nullable=False)
    room_type = db.Column(db.String(30), nullable=False)
    photo_url = db.Column(db.String(), nullable=True)

    def __init__(self, name, price, country, city, departure, nights, room_type, photo_url):
        self.name = name
        self.price = price
        self.country = country
        self.city = city
        self.departure = departure
        self.nights = nights
        self.room_type = room_type
        self.photo_url = photo_url


class Applications(db.Model):
    __tablename__ = "applications"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    message = db.Column(db.Text(), nullable=False)

    def __init__(self, phone, email, name, message):
        self.phone = phone
        self.email = email
        self.name = name
        self.message = message

# db.create_all()
# db.drop_all()

@app.route("/", methods=["GET"])
def show_home_page():
    countries = Countries.query.all()
    return render_template("index.html", is_home=True, countries=countries)


@app.route("/tour/<int:id>", methods=["GET"])
def show_tour_page(id):
    tour = Tours.query.get_or_404(id)
    return render_template("tour.html", tour=tour)


@app.route("/country/<int:id>", methods=["GET"])
def show_country_page(id):
    country = Countries.query.get_or_404(id)
    return render_template("country.html", country=country)


@app.route("/about", methods=["GET"])
def show_about_page():
    return render_template("about.html")


@app.route("/admin", methods=["GET"])
def show_admin_page():
    applications = Applications.query.all()
    return render_template("admin.html", applications=applications)


@app.route("/create-country", methods=["POST"])
def create_country():
    name = request.form['name']
    continent = request.form['continent']
    photo_url = request.form['photo_url']
    flag_url = request.form['flag_url']
    description = request.form['description']
    row = Countries(name, continent, photo_url, flag_url, description)
    db.session.add(row)
    db.session.commit()
    return render_template("admin.html")


@app.route("/create-tour", methods=["POST"])
def create_tour():
    name = request.form['name']
    price = request.form['price']
    country = request.form['country']
    city = request.form['city']
    departure = request.form['departure']
    nights = request.form['nights']
    room_type = request.form['room_type']
    photo_url = request.form['photo_url']
    row = Tours(name, price, country, city, departure,
                nights, room_type, photo_url)
    db.session.add(row)
    db.session.commit()
    return render_template("admin.html")


@app.route("/create-application", methods=["POST"])
def create_application():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    message = request.form['message']
    row = Applications(phone, email, name, message)
    db.session.add(row)
    db.session.commit()
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
