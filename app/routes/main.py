from flask import Blueprint, request

main = Blueprint('main', __name__)

@main.route("/", methods=['GET'])
def index():
    return {'message': f'Hello World'}
