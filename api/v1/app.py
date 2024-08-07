#!/usr/bin/python3
""" Flask Application """
from os import environ
import os
from flask import Flask
from models import storage
# from api.v1.views import app_views


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object('config')

    # Register blueprint here
    app.register_blueprint(app_views)

    @app.teardown_appcontext
    def teardown(exception):
        """Close the storage on teardown."""
        storage.close()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', 5000)),
            threaded=True)
