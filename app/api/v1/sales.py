from flask_restful import Resource
from flask_jwt import jwt_required


class ShowAllSales(Resource):
    @jwt_required()
    def get(self):
        return '', 204


class ShowSingleSale(Resource):
    @jwt_required()
    def get(self, transaction_id):
        return '', 204


class AddSale(Resource):
    @jwt_required()
    def post(self):
        return '', 204
