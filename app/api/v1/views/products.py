from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from ..utils import *
from flask_jwt_extended import (jwt_required)

parser = reqparse.RequestParser()
parser.add_argument('product_name', required=True, type=str, help='How about Product Name?')
parser.add_argument('quantity', required=True, type=int, help='How about Quantity?')
parser.add_argument('unit_price', required=True, type=float, help='How about Price?')
parser.add_argument('category', required=True, type=str, help='How about Category?')


class Products(Resource):
    @staticmethod
    @jwt_required
    def get():
        """Fetches all products"""
        if len(Product.products) >= 1:
            return make_response(jsonify(
                {
                    'status': 'OK',
                    'products': Product.get_all_products()
                }
            ), 200)
        return make_response(jsonify(
            {
                'message': 'No product found!'
            }
        ), 200)

    @staticmethod
    @jwt_required
    def post():
        """Create a product"""
        data = parser.parse_args()
        product_name = data['product_name']
        quantity = data['quantity']
        category = data['category']
        unit_price = data['unit_price']
        product_data = ProductValidation(product_name, quantity, category, unit_price)
        product_data.validate_product_data()
        new_product = Product(product_name=product_name,
                              quantity=quantity,
                              unit_price=unit_price,
                              category=category
                              )

        new_product.add_product()

        return make_response(jsonify({
            'status': 'success',
            'product_name': product_name,
            'quantity': quantity,
            'category': category,
            'unit_price': unit_price

        }), )


class GetSpecificProduct(Resource):

    @staticmethod
    @jwt_required
    def get(product_id):
        product = Product.get_specific_product(product_id)
        if product:
            return make_response(jsonify({'product': product}), 200)
        return make_response(jsonify("That product is not available!"), 404)
