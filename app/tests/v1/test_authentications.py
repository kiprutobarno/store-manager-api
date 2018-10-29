import unittest
from flask import json
from app import create_app


class TestAuthentication(unittest.TestCase):
    """Tests for user authentication"""

    def setUp(self):
        """Set up for configuration and testing env"""
        self.app = create_app('testing')
        self.test_client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.client = self.app.test_client()
        """dummy admin signup"""
        self.user_admin = json.dumps({
            "email": "admin@storemanager.com",
            "password": "admin@123",
            "role": "admin"
        })

        self.user_attendant = json.dumps({
            "email": "attendant@storemanager.com",
            "password": "attendant@123",
            "role": "attendant"
        })
        """dummy admin login"""
        self.login_admin = json.dumps({
            "email": "admin@storemanager.com",
            "password": "admin@123"
        })

        self.login_owner = json.dumps({
            "email": "owner@storemanager.com",
            "password": "owner@123"
        })

        self.login_attendant = json.dumps({
            "email": "attendant@storemanager.com",
            "password": "attendant@123"
        })

        """missing email signup"""
        self.missing_email_signup = json.dumps({
            "email": "",
            "password": "admin@123",
            "role": "admin"
        })

        """integer role"""
        self.non_string_role_signup = json.dumps({
            "email": "",
            "password": "admin@123",
            "role": 9
        })

        """already registered email signup"""
        self.already_registered_email_signup = json.dumps({
            "email": "admin@storemanager.com",
            "password": "admin@123",
            "role": "admin"
        })

        """Invalid email signup"""
        self.invalid_email_signup = json.dumps({
            "email": "admin.com",
            "password": "admin@123",
            "role": "admin"
        })

        """missing password signup"""
        self.missing_password_signup = json.dumps({
            "email": "adminly@storemanager.com",
            "password": "",
            "role": "admin"
        })

        """missing role signup"""
        self.missing_role_signup = json.dumps({
            "email": "adminly@storemanager.com",
            "password": "admin@1345",
            "role": ""
        })

        """missing email login"""
        self.missing_email = json.dumps({
            "email": "",
            "password": "attendant@123"
        })

        """missing password login"""
        self.missing_password = json.dumps({
            "email": "admin@storemanager.com",
            "password": ""
        })

        """wrong credentials login"""
        self.wrong_credentials = json.dumps({
            "email": "admin@storemanager.com",
            "password": "admn@1234"
        })

    def test_not_string_role_signup(self):
        new_user = self.client.post('/api/v1/signup', data=self.non_string_role_signup,
                                    content_type='application/json')
        self.assertEqual(new_user.status_code, 400)

    def test_invalid_email_signup(self):
        new_user = self.client.post('/api/v1/signup', data=self.invalid_email_signup,
                                    content_type='application/json')
        result = json.loads(new_user.data.decode())
        self.assertEqual(result["message"], "Invalid email address")
        self.assertEqual(new_user.status_code, 400)

    def test_already_registered_email_signup(self):
        new_user = self.client.post('/api/v1/signup', data=self.missing_email_signup,
                                    content_type='application/json')
        result = json.loads(new_user.data.decode())
        self.assertEqual(result["message"], "Invalid email address")
        self.assertEqual(new_user.status_code, 400)

    def test_missing_role_signup(self):
        new_user = self.client.post('/api/v1/signup', data=self.missing_role_signup,
                                    content_type='application/json')
        result = json.loads(new_user.data.decode())
        self.assertEqual(result["message"], "Role cannot be empty")
        self.assertEqual(new_user.status_code, 400)

    def test_missing_password_signup(self):
        new_user = self.client.post('/api/v1/signup', data=self.missing_password_signup,
                                    content_type='application/json')
        result = json.loads(new_user.data.decode())
        self.assertEqual(result["message"], "You must provide a password")
        self.assertEqual(new_user.status_code, 400)

    def test_admin_user_signup(self):
        new_user = self.client.post('/api/v1/signup', data=self.user_admin,
                                    content_type='application/json')
        result = json.loads(new_user.data.decode())
        self.assertEqual(result["message"], "User admin@storemanager.com was created")
        self.assertEqual(new_user.status_code, 201)

    def test_missing_email_login(self):
        """test missing email login"""
        user_admin_login = self.client.post('/api/v1/login', data=self.missing_email,
                                            content_type='application/json')
        self.assertEqual(user_admin_login.status_code, 400)

    def test_wrong_credentials_login(self):
        user_admin_login = self.client.post('/api/v1/login', data=self.wrong_credentials,
                                            content_type='application/json')
        result = json.loads(user_admin_login.data.decode())
        self.assertEqual(result["message"], "User does not exist!")
        self.assertEqual(user_admin_login.status_code, 200)

    def test_missing_password_login(self):
        """test missing email login"""
        user_admin_login = self.client.post('/api/v1/login', data=self.missing_password,
                                            content_type='application/json')
        self.assertEqual(user_admin_login.status_code, 400)

    def test_admin_login(self):
        """Test that an admin can login"""
        user_admin_login = self.client.post('/api/v1/login', data=self.login_admin,
                                            content_type='application/json')
        self.assertEqual(user_admin_login.status_code, 200)
        self.token_attendant = json.loads(user_admin_login.data.decode()).get("x-api-key")

    def test_attendant_user_signup(self):
        new_user = self.client.post('/api/v1/signup', data=self.user_attendant,
                                    content_type='application/json')
        result = json.loads(new_user.data.decode())
        self.assertEqual(result["message"], "User attendant@storemanager.com was created")
        self.assertEqual(new_user.status_code, 201)

    def test_attendant_login(self):
        """Test that an attendant can login"""
        user_attendant_login = self.client.post('/api/v1/login', data=self.login_attendant,
                                                content_type='application/json')
        self.assertEqual(user_attendant_login.status_code, 200)
        self.token_attendant = json.loads(user_attendant_login.data.decode()).get("x-api-key")

    def test_user_not_exist(self):
        user_login = self.client.post('/api/v1/login', data=self.login_owner,
                                      headers={'content-type': 'application/json'})
        response = json.loads(user_login.data.decode())
        self.assertEqual(response['message'], 'User does not exist!')
        self.assertEqual(user_login.status_code, 200)

    def test_user_login_non_existing_password(self):
        """Test that user cant login with incorrect password"""
        login = self.client.post('/api/v1/login', data=json.dumps({
            "email": "rabiot@storemanager.com",
            "password": "rabiot@him"}),
                                   headers={'content-type': 'application/json'})
        response = json.loads(login.data.decode())
        self.assertEqual(response['message'], 'User does not exist!')
        self.assertEqual(login.status_code, 200)

    def test_user_login_non_existing_username(self):
        """Test that user cant login with incorrect password"""
        login = self.client.post('/api/v1/login', data=json.dumps({
            "email": "rabiot@storemanager.com",
            "password": "rabiot@him"}),
                                   headers={'content-type': 'application/json'})

        response = json.loads(login.data.decode())
        self.assertEqual(response['message'], 'User does not exist!')
        self.assertEqual(login.status_code, 200)

    def tearDown(self):
        pass
