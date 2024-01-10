from flask import Flask
from flask_cors import CORS
from MilitaryDefenseApp.search.search_api import search_blueprint
from users.user_api import user_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app, origins='*')

    # Register the blueprints
    app.register_blueprint(search_blueprint, url_prefix='/api/')
    app.register_blueprint(user_blueprint, url_prefix='/api/')

    return app

if __name__ == '__main__':
    create_app().run(host='127.0.0.1', port=5000, debug=True)
