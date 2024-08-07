#!/usr/bin/python3
""" Blueprint for API """
from api.v1.views import index
from api.v1.views import states
from api.v1.views import places
from api.v1.views import places_reviews
from api.v1.views import cities
from api.v1.views import amenities
from api.v1.views import users
from api.v1.views import places_amenities
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import view modules here to avoid circular imports
