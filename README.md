# learning-flask
First looks into Flask

## Start in Develop
```commandline
FLASK_ENV=development FLASK_APP=src/application.py flask run

```

##TODO
### Basis
1. template einbinden
2. main-styles.css
3. api: gibt dictionary(json) zurück
4. javascript einbinden, was folgende Feature z.b implementiert:
    1. Button "Hello"
    2. Klick auf "Hello" => javascriot funktion doHello aufrufen und einen Modal (alert) "Hello world" anzeigem

### Stufe 2
1. für dictionary eigenen datei ablegen 

### Single Page with css, javascript and template
1. Create new Templates dogs.html
```
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Dogs</title>
  </head>
  <body>
    <div>
      <h1>The gallery of dogs</h1>
      <em>This is a Singlepage application using Flask, javascript, html and css</em>
      <hr/>
    </div>
  </body>
</html>

```
2. add new funtion to application.py
```
@app.route("/dogs/")
def dogs_index():
    return render_template('dogs.html')
```
