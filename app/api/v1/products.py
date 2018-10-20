from flask_restful import Resource


class ShowAllProducts(Resource):
    def get(self):
        return '', 204


class ShowSingleProduct(Resource):
    def get(self, product_id):
        return '', 204


class AddProduct(Resource):
    def post(self):
        return '', 204


class UpdateProduct(Resource):
    def put(self, product_id):
        return '', 204


class DeleteProduct(Resource):
    def delete(self, product_id):
        return '', 204
