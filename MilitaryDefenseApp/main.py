from flask import Flask
from MilitaryDefenseApp.search.search_api import search_blueprint
from users.user_api import user_blueprint

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(search_blueprint, url_prefix='/api/search')
app.register_blueprint(user_blueprint, url_prefix='/api/user')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
