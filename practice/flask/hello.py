from flask import Flask

app = Flask(__name__)

html = "<h1>hello</h1>"

@app.route("/")
def hello():
        return html