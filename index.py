from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Home Page Route"


@app.route("/about")
def about():
    return "About Page Route"


@app.route("/portfolio")
def portfolio():
    return "Portfolio Page Route"


@app.route("/contact")
def contact():
    return "Contact Page Route"
