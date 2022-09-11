#!/usr/bin/python3
"""
Script that starts a Flask web application listening on 0.0.0.0, port 5000 and
routes /: display “Hello HBNB!” with the option strict_slashes=False in the
route definition
"""

from flask import Flask
app = Flask(__name__)


# strict_slashes=False The control of the url address ending character "/"
# False: It can be accessed regardless of whether the ending "/" exists or not
@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
