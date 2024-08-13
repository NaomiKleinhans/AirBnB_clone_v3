#!/usr/bin/python3
"""API Blueprint for version 1 of the App.

This module initializes the Flask blueprint for version 1 of the API.
It sets the URL prefix for all routes under this version to '/api/v1'.
The blueprint is used to organize and register the various view modules
that handle specific endpoints of the API.
"""

from api.v1.views import cities
from api.v1.views import users
from api.v1.views import places
from api.v1.views import places_amenities
from flask import Blueprint

app_views = Blueprint('app_views', __name__)