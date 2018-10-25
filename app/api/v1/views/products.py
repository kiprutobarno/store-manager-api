from flask import jsonify, make_response, request
from flask_restful import Resource
from .users import token_required
from ..utils import *


class Product(Resource):

    # Get all products
    @token_required
    def get(self, current_user):
        if current_user:
            if len(products) < 1:
                response = make_response(jsonify({
                    'status': 'Failure',
                    'message': "The inventory is empty!"
                }), 404)
            else:
                response = make_response(jsonify({
                    'status': 'Ok',
                    'message': "Success",
                    'products': products
                }), 200)
        else:
            response = make_response(jsonify({
                'status': 'Failure',
                'message': "Your are not logged in!"
            }), 401)
        return response

    @token_required
    def post(self, current_user):
        data = request.get_json()
        if current_user and current_user['role'] != "admin":
            return make_response(jsonify({
                'status': 'Failure',
                'message': "You don't have admin rights, please contact admin!"
            }), 401)
        if current_user and current_user['role'] == "admin":
            valid_product = ProductValidation(data)
            valid_product.validate_product_details()
            product = Product(data)
            product.create_product()
            return make_response(jsonify({
                'status': 'OK',
                'message': "Product created Successfully",
                'products': products
            }), 201)


class SpecificProduct(Resource):
    @token_required
    def get(self, current_user, product_id):
        if current_user:
            for product in products:
                if product['product_id'] == int(product_id):
                    return make_response(jsonify({
                        'status': 'OK',
                        'message': "Success",
                        'product': product
                    }), 200)

            return make_response(jsonify({
                'status': 'Failure',
                'message': "Sorry, we do not stock that product"
            }), 404)



