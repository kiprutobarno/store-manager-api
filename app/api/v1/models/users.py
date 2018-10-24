from flask_jwt_extended import JWTManager
from flask import current_app as app
from passlib.hash import pbkdf2_sha256 as sha256
jwt = JWTManager(app)


class User(object):
    registered_users = []

    def __init__(self, username, password):
        self.user_id = len(self.registered_users) + 1
        self.username = username
        self.password = password

    def create_user(self):
        user = dict(user_id=self.user_id,
                    username=self.username,
                    password=self.password)
        self.registered_users.append(user)
        return user

    def get_all_users(self):
        return self.registered_users

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)




