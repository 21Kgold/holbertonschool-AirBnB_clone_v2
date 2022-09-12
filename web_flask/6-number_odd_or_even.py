#!/usr/bin/python3
"""
Script that starts a Flask web application listening on 0.0.0.0, port 5000 and
routes / display “Hello HBNB!” & /hbnb display "HBNB" with the option
strict_slashes=False in the route definition
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hello_world2():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_world3(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def hello_world4(text):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def hello_world5(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:page>", strict_slashes=False)
def hello_world6(page):
    return render_template("5-number.html", page=page)


@app.route("/number_odd_or_even/<int:page>", strict_slashes=False)
def hello_world7(page):
    check = ""
    if page % 2 == 0:
        check = "even"
        return render_template("6-number_odd_or_even.html",
                               check=check, page=page)
    else:
        check = "odd"
        return render_template("6-number_odd_or_even.html",
                               check=check, page=page)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
