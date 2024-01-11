from flask import Blueprint, jsonify, request
from flask_restful import Api
import os
from django.contrib.auth import authenticate
from django import setup as django_setup  # Import Django's setup function

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MilitaryDefenseApp.settings")

# Call Django's setup function
django_setup()

user_blueprint = Blueprint("user", __name__)
api = Api(user_blueprint)

@user_blueprint.route('/login', methods=['POST'])
def api_login():
    data = request.json

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
