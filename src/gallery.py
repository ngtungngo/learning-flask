from flask_cors import CORS, cross_origin
from flask import Flask, render_template, redirect
from markupsafe import escape

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
def hello():
    return redirect("/gallery/dogs", code=302)

@app.route("/gallery/<animal>")
async def gallery(animal):
    if escape(animal) == 'dogs':
        page_title = "Dog's gallery"
    else:
        page_title = "Cat\'s gallery"
    
    print(f'page_title: {page_title}')
    
    content = {
        'animal': animal,
        'page_title': page_title,
        'names': ['Ikarus', 'Ikaros', 'Karies', 'Sirius', 'Thanos', 'Suiris']    
    }
    
    return render_template('gallery.html', data=content)
