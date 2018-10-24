from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from app.api.v1.utils import *
from app.api.v1.models.users import *
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_refresh_token_required, get_jwt_identity)


parser = reqparse.RequestParser()
parser.add_argument('username', required=True, help='Username cannot be blank', type=str)
parser.add_argument('password', required=True, help='Password cannot be blank', type=str)


class Registration(Resource):
    def __init__(self):
        self.users = User.registered_users

    def post(self):
        data = parser.parse_args()
        username = data['username']
        password = data['password']
        validate_user_data = Validate(username, password)
        validate_user_data.validate_user_details()
        user = User(username=data['username'], password=User.generate_hash(data['password']))
        user.create_user()
        return make_response(jsonify({
            'status': 'success',
            'message': 'User {} was created'.format(data['username'])
        }), 201)

    def get(self):
        return make_response(jsonify({
            'users': self.users
        }))


class Login(Resource):
    def post(self):
        data = parser.parse_args()
        username = data['username']
        password = data['password']
        if not data or not username or not password:
            return make_response(jsonify({
                'status': 'Failed',
                'message': "User does not exist"
            }), 404)
        if len(User.registered_users) <= 0:
            return make_response(jsonify({
                'status': 'Failed',
                'message': "User does not exist"
            }), 404)
        for user in User.registered_users:

            if username == user["username"] and User.verify_hash(password, user['password']):
                access_token = create_access_token(identity=data['username'])
                refresh_token = create_refresh_token(identity=data['username'])
                return make_response(jsonify({
                    'status': 'success',
                    'message': 'Welcome {}'.format(username),
                    'access-token': access_token,
                    'refresh-token': refresh_token
                }))

            else:
                return make_response(jsonify({
                    'message': 'Wrong credentials'
                }))


class Tokens(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}


