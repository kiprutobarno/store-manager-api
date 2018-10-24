from flask import jsonify, request, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.api.v1.models.products import Inventory


class Product(Resource):
    def __init__(self):
        self.products = Inventory()

    @jwt_required
    def post(self):
        data = request.get_json()
        product_name = data['product_name']
        quantity = data['quantity']
        unit_price = data['unit_price']
        category = data['category']

        new_product = self.products.add_product(product_name, quantity, unit_price, category)
        return make_response(jsonify({'product:': new_product}), 201)

    @jwt_required
    def get(self):
        return make_response(jsonify({'products': self.products.get_all_products()}), 200)


class SpecificProduct(Resource):
    def __init__(self):
        self.products = Inventory()

    @jwt_required
    def get(self, product_id):
        product = self.products.get_specific_product(product_id)
        if product:
            return make_response(jsonify({'product': product}), 200)
        else:
            return make_response(jsonify("product no found!"), 404)

