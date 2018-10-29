from flask import abort
import re
from .models.user import User
from .models.product import *


class RegistrationValidation:
    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role

    def validate_user_data(self):
        """REGEX to verify email address format"""
        if re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email) is None:
            message = "Invalid email address"
            abort(400, message)
        for user in User.users:
            if self.email == user["email"]:
                message = "This email is already registered"
                abort(400, message)
        if self.email == "":
            message = "Your must provide an email address"
            abort(400, message)
        if self.password == "":
            message = "You must provide a password"
            abort(400, message)
        if self.role == "":
            message = "Role cannot be empty"
            abort(400, message)
        if type(self.email) != str:
            message = "Email address must be a string"
            abort(400, message)
        if self.role not in User.roles:
            message = "Role must either be admin or attendant"
            abort(400, message)
        if type(self.role) != str:
            message = "Role must be a string"
            abort(400, message)
        if len(self.password) <= 6:
            message = "Password must be at least 6 characters long"
            abort(400, message)
        elif not any(char.isdigit() for char in self.password):
            message = "Password must contain a digit"
            abort(400, message)
        elif not re.search("[#@$]", self.password):
            message = "Password must have one of the special character [#@$]'"
            abort(400, message)


class LoginValidation:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate_login_data(self):
        if self.email == "":
            message = "Email address cannot be empty"
            abort(400, message)
        if self.password == "":
            message = "Password cannot be empty"
            abort(400, message)
        if self.password and self.email == "":
            message = "Email address and Password required!"
            abort(400, message)


class ProductValidation:
    def __init__(self, product_name, quantity, category, unit_price):
        self.product_name = product_name
        self.quantity = quantity
        self.category = category
        self.unit_price = unit_price

    def validate_product_data(self):
        for product in Product.products:
            if product['product_name'] == self.product_name:
                message = "Sorry, '" + self.product_name + "' already exists"
                abort(400, message)

        if type(self.product_name) != str:
            message = "product name must be a string"
            abort(400, message)

        if self.product_name == '':
            message = "Product name cannot be empty"
            abort(400, message)

        if self.quantity < 0 or self.quantity == "":
            message = "quantity must be a positive integer"
            abort(400, message)

        if self.unit_price < 0:
            message = "price must be a positive float"
            abort(400, message)

        if type(self.category) != str:
            message = "Category must be a string"
            abort(400, message)

        if self.category == "":
            message = "Category cannot be empty"
            abort(400, message)

