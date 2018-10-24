from flask import jsonify, request, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required
# import sale class
from app.api.v1.models.sales import Sale


class SaleTransaction(Resource):
    def __init__(self):
        self.sales = Sale()

    @jwt_required
    def post(self):
        data = request.get_json()
        product_name = data['product_name']
        quantity = data['quantity']
        unit_price = data['unit_price']
        category = data['category']

        new_transaction = self.sales.create_sale(product_name, quantity, unit_price, category)
        return make_response(jsonify({'sale': new_transaction}), 201)

    @jwt_required
    def get(self):
        return make_response(jsonify({'sales': self.sales.get_all_sales()}), 200)


class SpecificSale(Resource):
    def __init__(self):
        self.sales = Sale()

    @jwt_required
    def get(self, transaction_id):
        sale = self.sales.get_specific_sale(transaction_id)
        if sale:
            return make_response(jsonify({'sale': sale}), 200)
        else:
            return make_response(jsonify("Transaction not found!"), 404)

