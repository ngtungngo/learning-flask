from flask_cors import CORS, cross_origin
from flask import Flask, render_template, jsonify

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/user")
def api():
    # TODO function aus eigebundenen Modulen (Datei) aufrufen
    return {
        "name": "Thien Minh",
        "age" : 16
    }


@app.route("/home/")
def home():
    return render_template('index.html')


@app.route("/<page_name>/")
def test(page_name):
    return render_template('test.html', page_name=page_name)


@app.route("/users/", methods=['GET'])
def user():
    users = [
        {
          "firstname": "Kevin",
          "surname": "Ngo",
          "birthday": "15.09.2021"
        },
        {
          "firstname": "Franz",
          "surname": "Friedrich",
          "birthday": "28.12.2021"
        },
        {
          "firstname": "Hans",
          "surname": "Walter",
          "birthday": "10.04.2022"
        },
        {
          "firstname": "Peter",
          "surname": "Ulrich",
          "birthday": "08.02.2020"
        },
        {
          "firstname": "Frieda",
          "surname": "Barin",
          "birthday": "01.02.2018"
        }
    ]
    return jsonify(users)


@app.route("/cars/", methods=['Get'])
def cars():
    cars = [
        {
            "brand": "Ford",
            "model": "Mustang",
            "year": "2018"
        },
        {
            "brand": "Porsche",
            "model": "944",
            "year": "1989"
        },
        {
            "brand": "Volkswagen",
            "model": "Polo II",
            "year": "1997"
        },
        {
            "brand": "Audi",
            "model": "e-tron GT",
            "year": "2021"
        }
    ]
    return jsonify(cars)

votes = 0

@app.route("/votes/")
def index_votes():
    return render_template('votes.html', votes=votes)

@app.route("/up", methods=["POST"])
def upvote():
    global votes
    votes = votes + 1
    return str(votes)

@app.route("/down", methods=["POST"])
def downvote():
    global votes
    if votes >= 1:
        votes = votes - 1
    return str(votes)


@app.route("/dogs/")
def dogs_index():
    dogs = ['Ikarus', 'Ikaros', 'Karies', 'Sirius', 'Thanos', 'Suiris']
    return render_template('dogs.html', dogs=dogs)

@app.route("/layout/")
def page_with_flex():
    return render_template('layout.html')

