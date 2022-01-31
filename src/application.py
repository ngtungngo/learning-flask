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
