from flask_cors import CORS, cross_origin
from flask import Flask, render_template, redirect

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
def hello():
    return redirect("/gallery/dogs", code=302)

@app.route("/gallery/<animal>")
def gallery(animal):
    
    if animal is 'dogs':
        url = 'https://dog.ceo/api/breeds/image/random'
    else:
        url = 'https://cat.ceo/api/breeds/image/random'
        
    content = {
        'animal': animal,
        'url': url,
        'names': ['Ikarus', 'Ikaros', 'Karies', 'Sirius', 'Thanos', 'Suiris']    
    }
    
    return render_template('gallery.html', data=content)
