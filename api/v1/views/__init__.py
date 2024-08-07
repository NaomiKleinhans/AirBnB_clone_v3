#!/usr/bin/python3
""" Blueprint for API """
from api.v1.views import (
    places_amenities,
    users,
    amenities,
    cities,
    places_reviews,
    places,
    states,
    index
)
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import views after the blueprint is created to avoid circular imports
