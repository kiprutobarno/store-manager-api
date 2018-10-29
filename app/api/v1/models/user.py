from passlib.hash import pbkdf2_sha256 as sha256
from flask import request
from functools import wraps
import jwt


class User(object):
    """User model"""
    users = []
    roles = ['admin', 'attendant']

    def __init__(self, email, password, role):
        self.user_id = len(self.users) + 1
        self.email = email
        self.password = password
        self.role = role

    def create_user(self):
        user = dict(user_id=self.user_id,
                    email=self.email,
                    password=self.password,
                    role=self.role)
        self.users.append(user)
        return user

    def get_all_users(self):
        return self.users

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hashed_password):
        return sha256.verify(password, hashed_password)


def jwt_required(f):
    @wraps(f)
    def decorated(*arg, **kwargs):
        token = None
        if 'x-api-key' in request.headers:
            token = request.headers['x-api-key']
        if not token:
            return {'result': 'token is missing'}, 401
        try:
            token = jwt.decode(token, 'sweet-secret', algorithms=['HS256']), 401
        except StandardError:
            return {'result': 'token is invalid'},401
        return f(*arg, **kwargs)
    return decorated
