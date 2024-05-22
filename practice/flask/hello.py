from flask import Flask

app = Flask(__name__)

"""
@app.route("/japan")
def japan():
    return "<p>Hello,Japan!<p>"

@app.route("/america")
def america():
    return "<p>Hello,America!<p>"

@app.route("/world")
def world():
    return "<p>Hello,World!<p>"
"""

@app.route("/japan/<city>")
def japan(city):
    return f"Hello, { city } in Japan!"
