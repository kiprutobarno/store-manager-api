from flask import jsonify, request, abort
from flask_restful import Resource
from flask_jwt import jwt_required


sales = [
    {
        'transaction_id': 1,
        'item': [
            {
                'product_id': 2,
                'quantity': 10,
                'unit_price': 10,
                'cost': 100
            }
        ],

        'total_cost': 150
    }
]


class ShowAllSales(Resource):
    @jwt_required()
    def get(self):
        return jsonify(
            {
                "Response": "success",
                "Status": "OK",
                'sales': sales
            }
        )


class ShowSingleSale(Resource):
    @jwt_required()
    def get(self, transaction_id):
        return '', 204


class AddSale(Resource):
    @jwt_required()
    def post(self):
        return '', 204
