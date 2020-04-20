from flask import Flask

app = Flask(__name__)

#handle requests to the home page.
@app.route("/")
def index():
    return "uWu!"

@app.route("/about")
def about():
    return "About me"
