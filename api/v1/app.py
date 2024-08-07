# api/v1/app.py
import os
from flask import Flask
from models import storage
from api.v1.views import app_views


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object('config')  # Ensure 'config' is available

    app.register_blueprint(app_views)  # Register the blueprint

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
