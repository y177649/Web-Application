from flask import Flask

app = Flask(__name__)

@app.route("/japan/<city>/")
def japan(city):
    return f"Hello, {city} in Japan!"