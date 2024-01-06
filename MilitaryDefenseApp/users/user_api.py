from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api
from django.contrib.auth import authenticate

user_blueprint = Blueprint("user", __name__)
api = Api(user_blueprint)

class AuthResource(Resource):
    def post(self):
        # Parse the incoming JSON data from the request body
        data = request.get_json()

        # Get the username and password from the request
        username = data.get("username")
        password = data.get("password")

        if username is None or password is None:
            # If any of the required fields is missing, return an error response
            response_data = {"error": "Missing required fields"}
            return jsonify(response_data), 400  # Bad Request

        # Authenticate the user using Django's authentication system
        user = authenticate(username=username, password=password)

        if user is not None:
            # Authentication successful
            response_data = {"message": "Authentication successful", "role": user.type}
            return jsonify(response_data)
        else:
            # Authentication failed
            response_data = {"message": "Authentication failed"}
            return jsonify(response_data), 401  # Unauthorized

# Define the API endpoint
api.add_resource(AuthResource, "/login")