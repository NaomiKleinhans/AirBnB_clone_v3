#!/usr/bin/python3
"""API Routes for Amenities.

This module defines the API routes for handling amenities in the Flask app.
It includes route handlers for retrieving all amenities for a place,
deleting an amenity from a place, and adding an amenity to a place.
"""

from flask import abort, jsonify, request
from models import storage
from models.engine.db_storage import classes
from api.v1.views import app_views

@app_views.route("/places/<place_id>/amenities", strict_slashes=False, methods=["GET"])
def get_amenities_place(place_id):
    """Get all amenities for a place."""
    # from api.v1.views import app_view
    place = storage.get(classes["Place"], place_id)
    if place is None:
        abort(404)

    amenities_list = [amenity.to_dict() for amenity in place.amenities]
    return jsonify(amenities_list)


@app_views.route("/places/<place_id>/amenities/<amenity_id>",
                 strict_slashes=False, methods=["DELETE"])
def delete_amenity_place(place_id, amenity_id):
    """Delete an amenity from a place."""
    # from api.v1.views import app_views
    place = storage.get(classes["Place"], place_id)
    if place is None:
        abort(404)

    amenity = storage.get(classes["Amenity"], amenity_id)
    if amenity is None:
        abort(404)
    if amenity not in place.amenities:
        abort(404)

    place.amenities.remove(amenity)  # Update to remove the association only
    storage.save()
    return jsonify({})


@app_views.route("/places/<place_id>/amenities/<amenity_id>",
                 strict_slashes=False, methods=["POST"])
def post_amenity_place(place_id, amenity_id):
    """Add an amenity to a place."""
    # from api.v1.views import app_views
    place = storage.get(classes["Place"], place_id)
    if place is None:
        abort(404)

    amenity = storage.get(classes["Amenity"], amenity_id)
    if amenity is None:
        abort(404)

    if amenity not in place.amenities:
        place.amenities.append(amenity)
        storage.save()
        return jsonify(amenity.to_dict()), 201

    return jsonify(amenity.to_dict()), 200
