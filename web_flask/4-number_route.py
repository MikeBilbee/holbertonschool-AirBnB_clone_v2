#!/usr/bin/python3
""" Starts a Flask web app with 5 routes"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    try:
        n = int(n)
        return 'n is a number'
    except ValueError:
        return 'n is not a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
