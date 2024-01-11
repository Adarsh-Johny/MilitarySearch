from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy()

CORS(app, origins='*')

import os

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
