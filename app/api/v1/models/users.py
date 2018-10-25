from werkzeug.security import generate_password_hash

users = []


class User:
    def __init__(self, data):
        self.username = data['username']
        self.role = data['role']
        self.password = generate_password_hash(data['password'], method='sha256')

    def create_user(self):
        user_id = len(users) + 1
        user = {
            'id': user_id,
            'username': self.username,
            'role': self.role,
            'password': self.password
        }
        users.append(user)
