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


class UserModel(db.Model):
    __tablename__ = 'users_user'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    password = db.Column(db.String(128), nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)
    is_superuser = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    first_name = db.Column(db.String(150), nullable=True)
    last_name = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(254), nullable=True)
    is_staff = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    date_joined = db.Column(db.DateTime, nullable=True)
    type = db.Column(db.String(50), default='ADMIN', nullable=False)
    rank = db.Column(db.String(50), nullable=True)
    unit = db.Column(db.String(100), nullable=True)
    gender = db.Column(db.String(50), nullable=True)
    dateEnlisted = db.Column(db.String(50), nullable=True)
    dateDischarged = db.Column(db.String(50), nullable=True)
    previousTraining = db.Column(db.String(50), nullable=True)
    awards = db.Column(db.String(50), nullable=True)