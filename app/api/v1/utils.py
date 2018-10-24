from flask import abort
from ..v1.models.users import *


class Validate:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate_user_details(self):
        for user in User.registered_users:
            if self.username == user["username"]:
                message = "Username already taken"
                abort(406, message)
        if len(self.password) <= 6 or len(self.password) > 12:
            message = "Password is too short"
            abort(400, message)
