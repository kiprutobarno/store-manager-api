from flask import jsonify, abort
from flask_restful import Resource
from flask_jwt import jwt_required


products = [
    {
        'product_id': 1,
        'name': 'banana',
        'category': 'fruit',
        'price': 35
    },
    {
        'product_id': 2,
        'name': 'carrots',
        'category': 'vegetable',
        'price': 30
    }
]


class ShowAllProducts(Resource):
    @jwt_required()
    def get(self):
        return products


class ShowSingleProduct(Resource):
    @jwt_required()
    def get(self, product_id):
        product = [product for product in products if product['product_id'] == product_id]
        if len(product) == 0:
            abort(404)
        return jsonify(
            {
                "Response": "success",
                "Status": "OK",
                'product': product[0]
            }
        )


class AddProduct(Resource):
    @jwt_required()
    def post(self):
        return '', 204


class UpdateProduct(Resource):
    @jwt_required()
    def put(self, product_id):
        return '', 204


class DeleteProduct(Resource):
    @jwt_required()
    def delete(self, product_id):
        return '', 204
