#!/usr/bin/python3
"""Flask web server to handle API requests.

This module sets up a Flask web server that handles API requests.
It registers the necessary routes and configurations
to respond to HTTP requests.
The server listens on the specified host and port,
which can be customized through environment variables.
"""

from api.v1.views import app_views
from flask import Blueprint, Flask, jsonify
from flask_cors import CORS
from models import storage
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')
app.url_map.strict_slashes = False

CORS(app, origins="0.0.0.0")

api_host = getenv("HBNB_API_HOST", "0.0.0.0")
api_port = getenv("HBNB_API_PORT", 5000)


@app.teardown_appcontext
def teardown(self):
    """Closes the database storage connection."""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors and returns a JSON-formatted 404 response."""
    return jsonify({"error": "Not found"}), 404


@app.route('/print-routes')
def print_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append(f"{rule.endpoint}: {rule}")
    return jsonify(routes)

if __name__ == "__main__":
   app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"), port=int(
       getenv("HBNB_API_PORT", 5000)), threaded=True)
