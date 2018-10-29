from flask_restful import Resource, reqparse
from flask import make_response, jsonify
from ..models.sale import *
from ..utils import *
from ..models.user import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('product_name', required=True, type=str, help='How about Product Name?')
parser.add_argument('quantity', required=True, type=int, help='How about Quantity?')
parser.add_argument('unit_price', required=True, type=float, help='How about Price?')
parser.add_argument('category', required=True, type=str, help='How about Category?')


class Sales(Resource):
    @staticmethod
    @jwt_required
    def get():
        """Fetches all sales"""
        if len(Sale.sales) >= 1:
            return make_response(jsonify(
                {
                    'status': 'OK',
                    'products': Sale.get_all_sales()
                }
            ), 200)
        else:
            return make_response(jsonify(
                {
                    'message': 'No product found!'
                }
            ), 200)

    @staticmethod
    @jwt_required
    def post():
        """Make a sale"""
        data = parser.parse_args()
        product_name = data['product_name']
        quantity = data['quantity']
        category = data['category']
        unit_price = data['unit_price']
        product_data = ProductValidation(product_name, quantity, category, unit_price)
        product_data.validate_product_data()
        new_sale = Sale(product_name=product_name,
                        quantity=quantity,
                        unit_price=unit_price,
                        category=category
                        )

        new_sale.make_sale()

        return make_response(jsonify({
            'status': 'success',
            'product_name': product_name,
            'quantity': quantity,
            'category': category,
            'unit_price': unit_price

        }), 201)


class GetSpecificSale(Resource):

    @staticmethod
    @jwt_required
    def get(transaction_id):
        sale = Sale.get_specific_sale(transaction_id)
        if sale:
            return make_response(jsonify({'sale': sale}), 200)
        else:
            return make_response(jsonify("Sale transaction not found"), 404)