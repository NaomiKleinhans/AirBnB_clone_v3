from flask import Blueprint

# Create Blueprint
app_views = Blueprint('app_views', __name__)

# Import view modules here
from api.v1.views import places_amenities
from api.v1.views import places
from api.v1.views import users
from api.v1.views import cities
