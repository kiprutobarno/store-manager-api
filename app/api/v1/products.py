from flask import jsonify, abort, request
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


# admin and an attendant should be able to retrieve all products
class ShowAllProducts(Resource):
    # @jwt_required()
    def get(self):
        return products


# store attendant and admin
class ShowSingleProduct(Resource):
    # @jwt_required()
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


# an admin and an attendant
class AddProduct(Resource):
    # @jwt_required()
    def post(self):
        product = {
            'product_id': products[-1]['product_id'] + 1,
            'name': request.json['name'],
            'category': request.json['category'],
            'price': request.json['price']
        }
        products.append(product)
        return {
            "Response": "Success",
            "Status": "Created",
            "product": product
        }


class UpdateProduct(Resource):
    # @jwt_required()
    def put(self, product_id):
        product = [product for product in products if (product['product_id'] == product_id)]

        if 'name' in request.json:
            product[0]['name'] = request.json['name']

        if 'category' in request.json:
            product[0]['category'] = request.json['category']

        if 'price' in request.json:
            product[0]['price'] = request.json['price']

        return jsonify(
            {
                "Response": "Success",
                "Status": "OK",
                'product': product[0]
            }
        )


class DeleteProduct(Resource):
    # @jwt_required()
    def delete(self, product_id):
        product = [product for product in products if (product['product_id'] == product_id)]
        products.remove(product[0])
        return jsonify(
            {
                "Response": "Success",
                "Status": "OK"
            }, 200
        )
