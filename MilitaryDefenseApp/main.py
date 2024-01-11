from flask_cors import CORS
from MilitaryDefenseApp.search.search_api import search_blueprint
from users.user_api import user_blueprint
from db_api import db_api_blueprint
from app import app

def create_app():
    CORS(app, origins='*')

    # Register the blueprints with different URL prefixes
    app.register_blueprint(search_blueprint, url_prefix='/api/')
    app.register_blueprint(user_blueprint, url_prefix='/api/')
    app.register_blueprint(db_api_blueprint, url_prefix='/api/')
    
    return app

if __name__ == '__main__':
    # Run the app
    create_app().run(host='127.0.0.1', port=5000, debug=True)