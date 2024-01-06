from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from django.contrib.auth import authenticate
# from .models import User

app = Flask(__name__)
api = Api(app)

# Set up Django settings
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MilitaryDefenseApp/MilitaryDefenseApp/settings.py")
# import django
# django.setup()


# Request parser for handling user input
parser = reqparse.RequestParser()
parser.add_argument("username", type=str, help="Username is required", required=True)
parser.add_argument("password", type=str, help="Password is required", required=True)


class AuthResource(Resource):
    def post(self):
        # Parse the incoming JSON data
        args = parser.parse_args()

        # Get the username and password from the request
        username = args["username"]
        password = args["password"]

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
api.add_resource(AuthResource, "/api/auth")

if __name__ == "__main__":
    app.run(debug=True)
