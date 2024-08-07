#!/usr/bin/python3
""" Blueprint for API """
from api.v1.views.index import register_routes as register_index
from api.v1.views.states import register_routes as register_states
from api.v1.views.places import register_routes as register_places
from api.v1.views.places_reviews import register_routes as register_places_reviews
from api.v1.views.cities import register_routes as register_cities
from api.v1.views.amenities import register_routes as register_amenities
from api.v1.views.users import register_routes as register_users
from api.v1.views.places_amenities import register_routes as register_places_amenities
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import and register view modules

# Register routes with app_views
register_places_amenities(app_views)
register_users(app_views)
register_amenities(app_views)
register_cities(app_views)
register_places_reviews(app_views)
register_places(app_views)
register_states(app_views)
register_index(app_views)
