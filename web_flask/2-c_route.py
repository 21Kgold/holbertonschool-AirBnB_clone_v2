#!/usr/bin/python3
"""
Script that starts a Flask web application listening on 0.0.0.0, port 5000 and
routes / display “Hello HBNB!” & /hbnb display "HBNB" with the option
strict_slashes=False in the route definition
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hello_world2():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_world3(text):
    new_text = text.replace("_", " ")
    return f"C {new_text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
