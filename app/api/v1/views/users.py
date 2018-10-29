from flask_restful import Resource, reqparse
from flask import make_response, jsonify
from app.api.v1.utils import *
from ..models.user import *
from flask_jwt_extended import (create_access_token)

parser = reqparse.RequestParser()
parser.add_argument('email', required=True, type=str, help='Email cannot be blank')
parser.add_argument('password', required=True, type=str)
parser.add_argument('role', type=str)


class SignUp(Resource):
    """Creates a user and returns a confirmation message"""
    def __init__(self):
        self.users = User.users

    @staticmethod
    def post():
        data = parser.parse_args()
        email = data['email']
        password = data['password']
        role = data['role']
        user_data = RegistrationValidation(email, password, role)
        user_data.validate_user_data()
        new_user = User(email=email, password=User.generate_hash(password), role=role)
        new_user.create_user()
        return make_response(jsonify({
            'status': 'success',
            'message': 'User {} was created'.format(email)
        }), 201)


class Login(Resource):
    """logs in registered users and returns a token and confirmation message"""
    def __init__(self):
        self.users = User.users

    @staticmethod
    def post():
        data = parser.parse_args()
        email = data['email']
        password = data['password']
        login_data = LoginValidation(email, password)
        login_data.validate_login_data()

        for user in User.users:
            if email == user["email"] and User.verify_hash(password, user['password']):
                access_token = create_access_token(identity=email)
                return jsonify(token=access_token, message="Login successful!")
        return jsonify(message="User does not exist!")
