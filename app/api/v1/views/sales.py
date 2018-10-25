from flask import jsonify, make_response, request
from flask_restful import Resource
from .users import token_required
from ..utils import *
from ..models.sales import *


class Sale(Resource):
    @token_required
    def get(self, current_user):
        if current_user['role'] == "admin":
            if len(sales) > 0:
                response = make_response(jsonify({
                    'status': 'OK',
                    'message': "Success",
                    'Sale': sales
                }), 200)
            else:
                response = make_response(jsonify({
                    'status': 'Failure',
                    'message': "No sale transaction found!"
                }), 404)
            return response

        return make_response(jsonify({
            'status': 'Failure',
            'message': "You do not have admin rights!"
        }), 403)

    # Make a sales
    @token_required
    def post(self, current_user):
        total = 0
        data = request.get_json()
        if not data:
            return make_response(jsonify({
                                         'status': 'Failure',
                                         'message': "No data!"
                                         }), 400)
        product_id = data['product_id']
        if current_user['role'] == 'attendant':
            for product in products:
                if product['quantity'] > 0:
                    if product['product_id'] == product_id:
                        attendant_id = current_user['user_id']
                        sale = {
                            'sale_id': len(sales) + 1,
                            'attendant_id': attendant_id,
                            'product': product
                        }
                        post_sale = Sale(sale)
                        post_sale.create_sale()
                        product['quantity'] = product['quantity'] - 1
                        for sale in sales:
                            if product['product_id'] in sale.values():
                                total = total + int(product['unit_price'])
                        return make_response(jsonify({
                            'status': 'OK',
                            'message': "Success",
                            'sales': sales,
                            "total": total
                        }), 201)
                    else:
                        return make_response(jsonify({
                            'Status': 'Failed',
                            'Message': "product does not exist"
                        }), 404)
                else:
                    return make_response(jsonify({
                                         'status': 'Failure',
                                         'message': "We've run out of stock!"
                                         }), 404)
        else:
            return make_response(jsonify({
                                         'status': 'Failure',
                                         'Message': "You are not an attendant"
                                         }), 403)


class SpecificSale(Resource):
    @token_required
    def get(self, current_user, sale_id):
        for sale in sales:
            if current_user['user_id'] == sale['attendant_id'] or current_user['role'] == 'admin':
                if int(sale_id) == sale['sale_id']:
                    response = make_response(jsonify({
                        'status': 'OK',
                        'message': "success",
                        'sale': sale
                    }), 200)

                else:
                    response = make_response(jsonify({
                        'status': 'Failure',
                        'message': "No sale transactions!"
                    }), 404)
                return response
            else:
                return make_response(jsonify({
                    'status': 'Failure',
                    'message': "You are not authorized to access this data"
                }), 401)
