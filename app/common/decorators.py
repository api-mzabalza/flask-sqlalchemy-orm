from flask import request, jsonify, current_app
from app.models.user import User
from app.schemas.user import user_schema
from functools import wraps
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        print('mike')

        bearer = request.headers.get('Authorization')
        if not bearer:
            return jsonify({'message': 'Token is missing'}), 401

        token = bearer.split(' ')[1].strip('"')
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        except Exception as e:
            return jsonify({'message': f'Token is invalid: {e}'}), 401

        rtn = User.query.filter_by(id=data['id']).all()

        if not rtn:
            return {
                'token': False,
                'message': 'User doesnt exist'
            }

        loged_user = user_schema.dump(rtn[0])
        return f(loged_user, *args, **kwargs)

    return decorated