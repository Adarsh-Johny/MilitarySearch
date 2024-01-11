from flask import Blueprint , jsonify
from db_models import MilitaryCampDbModel,UserModel

db_api_blueprint = Blueprint('db_api', __name__, url_prefix='')

@db_api_blueprint.route('military-camps', methods=['GET'])
def get_military_camps():
    military_camps = MilitaryCampDbModel.query.all()
    camps_list = [{
        'id': camp.id,
        'location': camp.location,
        'latitude': camp.latitude,
        'longitude': camp.longitude,
        'executes_action': camp.executes_action,
        'status': camp.status, 
        'service_branch': camp.service_branch
        } for camp in military_camps]
    
    return jsonify(camps_list)


@db_api_blueprint.route('users', methods=['GET'])
def get_users():
    users = UserModel.query.all()
    users_list = [{
        'userName': user.username,
        'firstName': user.first_name,
        'LastName': user.last_name,
        'email': user.email,
        'status': user.is_active,
        'type': user.type,
        } for user in users]
    
    return jsonify(users_list)