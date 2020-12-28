from flask import Blueprint, current_app, request, jsonify
from app import db, bcrypt
from app.models.user import User
from app.schemas.auth import login_schema
from app.schemas.user import user_registration_schema, user_schema
import datetime
import jwt


auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['POST'])
def login():
    errors = login_schema.validate(request.get_json())
    if errors:
        return {'message': 'Error','Error': errors}
    
    email = request.get_json()['email']
    password = request.get_json()['password']
    rtn = User.query.filter_by(email=email).all()

    if not rtn:
        return {
            'token': False,
            'message': 'Wrong Username'
        }

    user = user_schema.dump(rtn[0])
    
    if user and bcrypt.check_password_hash(user['password'], password):
        
        token = jwt.encode({'id': user['id'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, current_app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({
            'token': token,
            **user_registration_schema.dump(user)
        })

    return {
        'token': False,
        'message': 'Wrong Password'
    }