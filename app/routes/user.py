from flask import Blueprint, request
from app import db, bcrypt
from app.models.user import User
from app.schemas.user import user_registration_schema, user_delete_schema, user_edit_schema, user_schema
from app.common.decorators import token_required

users = Blueprint('users', __name__)



@users.route("/<user_id>", methods=['GET'])
def getUserByIdError(user_id):
    if type(user_id) != int:
        return {
            'status': False,
            'message': 'Wrong user id. Needs to be integer'
    }


@users.route("/<int:user_id>", methods=['GET'])
@token_required
def getUserById(loged_user, user_id):
    '''
    Gell user by id
    '''
    # print(user_id)
    rtn = User.query.filter_by(id=user_id).all()
    if not rtn:
        return {
            'status': False,
            'message': 'Wrong user id'
        }

    user = user_registration_schema.dump(rtn[0])
    
    return {
        'status': True,
        'user': user
    }

@users.route("/", methods=['GET'])
def getAll():
    '''
    Gell all users
    '''
    users = User.query.all()
    data = [user_registration_schema.dump(user) for user in users]
    return {
        'status': True,
        'data': data
    }



@users.route("/", methods=['DELETE'])
def delete():
    '''
    Delete existing user
    '''
    errors = user_delete_schema.validate(request.get_json())
    if errors:
        return {'message': 'Error','Error': errors}
    id = request.get_json()['id']

    try:
        user = User.query.filter(User.id==id).delete()
        db.session.commit()

    except Exception as e:
        return {'message': f'Error', 'Error': str(e)}
    
    if user:
        return {
            'status': True,
            'message': f'Deleted user with id: {id}'
        }
    return {
        'status': False,
        'message': f'User not found for id: {id}'
    }
    

@token_required
@users.route("/", methods=['POST'])
def add():
    '''
    Add new user
    '''
    errors = user_registration_schema.validate(request.get_json())

    if errors:
        return {
            'message': 'Error',
            'Error': errors
        }

    name = request.get_json()['name']
    email = request.get_json()['email']
    phone = request.get_json()['phone']
    password = request.get_json()['password']
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    user = User(name=name, email=email, phone=phone, password=hashed_password)

    try:
        db.session.add(user)
        db.session.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return {'message': f'Error', 'Error': error}

    return {
        'status' : True,
        'message': user_registration_schema.dump(user)
    }



## TODO: add hashed password updated
@users.route("/", methods=['PUT'])
def edit():
    '''
    Edit existing user
    '''
    input_data = request.get_json()
    errors = user_edit_schema.validate(input_data)
    if errors:
        return {'message': 'Error','Error': errors}
    if input_data.get('password'):
        input_data['password'] = bcrypt.generate_password_hash(input_data['password']).decode('utf-8')

    rtn = User.query.filter_by(id=input_data['id']).update(input_data)
    
    db.session.commit()

    if rtn:
        return {
            'status' : True,
            'message': f"Edited user with id: {input_data['id']}"
        }

    return {
        'status': False,
        'message': f'User not found for id: {id}'
    }
    


