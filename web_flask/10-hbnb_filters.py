#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """teardown sesh"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display filters"""
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    cities = sorted(storage.all("City").values(), key=lambda x: x.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
