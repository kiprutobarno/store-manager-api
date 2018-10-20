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
        def post(self):
            data = request.get_json()
            sale = {

                'transaction_id': len(sales) + 1,
                'item': [
                    {
                        'product_id': data['item'][0]['product_id'],
                        'quantity': data['item'][0]['quantity'],
                        'unit_price': data['item'][0]['unit_price'],
                        'cost': data['item'][0]['cost']
                    }
                ],
                'total_cost': data['total_cost']
            }
            sales.append(sale)
            return {
                "Response": "Success",
                "Status": "Created",
                "sale": sale
            }
