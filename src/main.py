from flask_cors import CORS, cross_origin
from flask import Flask, render_template, redirect, request
from markupsafe import escape
import names

app = Flask(__name__)
CORS(app, support_credentials=True)

numbers = 8

@app.route('/')
def hello():
    return redirect("/gallery/dogs", code=302)

@app.route("/gallery/<animal>")
def gallery(animal):
    if escape(animal) == 'dogs':
        page_title = "Dog's gallery"
    else:
        page_title = "Cat\'s gallery"
    
    print(f'page_title: {page_title}')
    
    content = {
        'animal': animal,
        'page_title': page_title,
        'numberspython wsgi.py': numbers,
        'names': [names.get_first_name(n) for n in range(numbers)]
    }
    
    return render_template('gallery.html', data=content)

@app.route("/gallery/<animal>", methods=['POST'])
def gallery_submit(animal):
    global numbers
    numbers = int(request.form['numbers'])
    print(f"number: {numbers}")
    return redirect(f"/gallery/{escape(animal)}", code=302)
    