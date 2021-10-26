from os import name
from  flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('ListadoPeliculas.html') 