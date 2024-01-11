from sqlalchemy import true
from app import db

class MilitaryCampDbModel(db.Model):
    __tablename__ = 'users_militarycamp'

    id = db.Column(db.Integer, nullable=False, primary_key=true)
    location = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    executes_action = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    service_branch = db.Column(db.String(50), nullable=False)