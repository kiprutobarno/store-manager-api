from flask_restful import Resource
from flask_jwt import jwt_required


class ShowAllProducts(Resource):
    @jwt_required()
    def get(self):
        return '', 204


class ShowSingleProduct(Resource):
    @jwt_required()
    def get(self, product_id):
        return '', 204


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