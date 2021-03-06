from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def home(first, second, third):
    return "Hello, World!"


@app.route("/api")
def api():
    return "API!"


if __name__ == "__main__":
    app.run(debug=True, port=3000)
