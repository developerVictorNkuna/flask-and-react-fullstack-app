from  flask import Flask
app = Flask(__name__,
    static_folder="./public",
    template_folder="./static")

# import templates.hello.views
from templates.hello.views import hello_blueprint

#register the blueprint

app.register_blueprint(hello_blueprint)