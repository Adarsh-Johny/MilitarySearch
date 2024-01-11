from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")

from django.contrib.auth import authenticate

user_blueprint = Blueprint("user", __name__)
api = Api(user_blueprint)

class AuthResource(Resource):
    def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if username is None or password is None:
            response_data = {"error": "Missing required fields"}
            return response_data, 400

        user = authenticate(username=username, password=password)

        if user is not None:
            response_data = {"message": "Authentication successful", "role": user.type}
            return jsonify(response_data)
        else:
            response_data = {"message": "Authentication failed"}
            return response_data, 401

# Define the API endpoint
api.add_resource(AuthResource, "/login")
