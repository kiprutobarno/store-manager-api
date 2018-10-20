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
    },
{
        'transaction_id': 2,
        'item': [
            {
                'product_id': 3,
                'quantity': 5,
                'unit_price': 400,
                'cost': 200
            }
        ],

        'total_cost': 200
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
        sale = [sale for sale in sales if sale['transaction_id'] == transaction_id]
        if len(sale) == 0:
            abort(404)
        return jsonify(
            {
                "Response": "success",
                "Status": "OK",
                'sale': sale[0]
            }
        )


class AddSale(Resource):
    @jwt_required()
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
