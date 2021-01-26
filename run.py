from flask import Flask
from templates import app
#Load this config object for development mode
#app.config.from_object("configurations.DevelopmentConfig")

app =Flask(__name__)
@app.route("/")


#we going to define the function for the above route/components/ui

def hello_world():
    return "Hello to the world of Flask"

if __name__ == "__main__":
    app.run(DEBUG=True)