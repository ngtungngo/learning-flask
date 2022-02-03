from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/user")
def user():
    # TODO function aus eigebundenen Modulen (Datei) aufrufen
    return {
        "name": "Thien Minh",
        "age" : 16
    }


@app.route("/home/")
def home():
    return render_template('layout.html')


@app.route("/<name>")
def test(name):
    return render_template('test.html', content=name)

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