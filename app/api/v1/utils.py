from flask import abort

from .models.users import *
from .models.products import *


class UserValidation:
    def __init__(self, data):
        self.username = data['username']
        self.password = data['password']
        self.role = data['role']

    def validate_user_details(self):
        if self.username == "":
            warning = "please provide your username"
            abort(400, warning)
        if self.password == "":
            warning = "please enter your password"
            abort(400, warning)
        if self.role == "":
            warning = "Please assign user role"
            abort(400, warning)
        for user in users:
            if self.username == user["username"]:
                warning = "Username already taken"
                abort(406, warning)
        if len(self.password) <= 6:
            warning = "Password must be at least 6 characters"
            abort(400, warning)
        elif not any(char.isdigit() for char in self.password):
            warning = "Password must have a digit"
            abort(400, warning)


class ProductValidation:
    def __init__(self, data):
        self.product_name = data['product_name']
        self.category = data['category']
        self.quantity = data['quantity']
        self.unit_price = data['unit_price']
        self.inventory = data['inventory']

    def validate_product_details(self):
        for product in products:
            if product['product_name'] == self.product_name:
                warning = "Sorry, product: '" + self.product_name + "' has been added already!"
                abort(406, warning)

        if type(self.product_name) != str:
            warning = "Sorry, product title must be a string"
            abort(400, warning)

        if type(self.category) != str:
            warning = "Sorry, product Category must be a string"
            abort(400, warning)
        if type(self.quantity) != int:
            warning = "Sorry, product quantity price must be an integer "
            abort(400, warning)
        if self.quantity < 0:
            warning = "Sorry, product quantity should be a positive value value"
            abort(400, warning)

        if type(self.unit_price) != float:
            warning = "Sorry, product unit price must be of the format 00.00"
            abort(400, warning)
        if self.unit_price < 0:
            warning = "Sorry, unit price should be a positive value"
            abort(400, warning)

        if type(self.inventory) != int:
            warning = "An inventory record must be an integer"
            abort(400, warning)
        if self.inventory < 0:
            warning = "Product price should be a positive value"
            abort(400, warning)
        if self.inventory < self.quantity:
            warning = "Sorry, we've ran out of stock"
            abort(400, warning)