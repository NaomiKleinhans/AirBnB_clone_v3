#!/usr/bin/python3
"""API Routes for Amenities.

This module defines the API routes for handling amenities in the Flask app.
It includes route handlers for retrieving all amenities,
retrieving a specific amenity by ID, creating a new amenity,
updating an existing amenity, and deleting an amenity.

Routes:
- GET /amenities: Retrieve all amenities.
- GET /amenities/<amenity_id>: Retrieve a specific amenity by ID.
- DELETE /amenities/<amenity_id>: Delete an amenity.
- POST /amenities: Create a new amenity.
- PUT /amenities/<amenity_id>: Update an existing amenity.
"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.engine.db_storage import classes


@app_views.route("/amenities", strict_slashes=False, methods=["GET"])
def get_amenities():
    """Retrieve all amenities."""
    amenities = storage.all("Amenity")
    amenities_list = [amenity.to_dict() for amenity in amenities.values()]
    return jsonify(amenities_list)


@app_views.route("/amenities/<amenity_id>", strict_slashes=False, methods=["GET"])
def get_amenity(amenity_id):
    """Retrieve a specific amenity by ID."""
    amenity = storage.get(classes["Amenity"], amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route("/amenities/<amenity_id>", strict_slashes=False, methods=["DELETE"])
def delete_amenity(amenity_id):
    """Delete an amenity."""
    amenity = storage.get(classes["Amenity"], amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({})


@app_views.route("/amenities", strict_slashes=False, methods=["POST"])
def post_amenity():
    """Create a new amenity."""
    amenity_data = request.get_json(silent=True)
    if not isinstance(amenity_data, dict):
        abort(400, "Not a JSON")
    if "name" not in amenity_data:
        abort(400, "Missing name")

    amenity = classes["Amenity"](**amenity_data)
    storage.new(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route("/amenities/<amenity_id>", strict_slashes=False, methods=["PUT"])
def put_amenity(amenity_id):
    """Update an existing amenity."""
    amenity = storage.get(classes["Amenity"], amenity_id)
    if amenity is None:
        abort(404)

    amenity_data = request.get_json(silent=True)
    if not isinstance(amenity_data, dict):
        abort(400, "Not a JSON")

    for key, value in amenity_data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict())
