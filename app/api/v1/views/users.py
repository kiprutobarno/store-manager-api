import datetime
from functools import wraps
from flask import jsonify, make_response, request
from flask_restful import Resource
from Instance.config import app_config
from werkzeug.security import check_password_hash
import jwt
from ..utils import *
from ..models.users import *


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        current_user = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return make_response(jsonify({
                'Message': 'Token is missing, You must login first'
            }), 401)
        try:
            data = jwt.decode(token, app_config['development'].SECRET_KEY)
            for user in users:
                if user['username'] == data['username']:
                    current_user = user
        except:
            return make_response(jsonify({'Message': 'Token is invalid'}),
                                 403)
        return f(current_user, *args, **kwargs)
    return decorated


class Registration(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({
                'Status': 'Fail',
                'Message': "You did not submit any data"
            }), 400)

        validate = UserValidation(data)
        validate.validate_user_details()
        user = User(data)
        user.create_user()
        for user in users:
            username = user['username']
            role = user['role']
            return make_response(jsonify({
                'Status': 'Success',
                'Message': "User '" + username + "' successfully registered as '" + role,
            }), 201)


class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        if not data or not username or not password:
            return make_response(jsonify({
                                         'Status': 'Failure',
                                         'Message': "You must log in first"
                                         }), 400)

        for user in users:
            if user['username'] == username and check_password_hash(user["password"],
                                                                    password):
                token = jwt.encode({'username': user['username'],
                                    'exp': datetime.datetime.utcnow() +
                                    datetime.timedelta(minutes=20)},
                                   app_config['development'].SECRET_KEY)
                return make_response(jsonify({
                                             'token': token.decode('UTF-8')
                                             }), 200)

        return make_response(jsonify({
            'Status': 'Failure',
            'Message': "Invalid login credentials"
        }), 404)
