from templates import app
from flask import render_template
@app.route("/") #we defining a route url,or user components,a section of the website app
@app.route("/hello")

def index():
    return render_template("index.html")