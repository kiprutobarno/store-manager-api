from flask_restful import Resource


class ShowAllSales(Resource):
    def get(self):
        return '', 204


class ShowSingleSale(Resource):
    def get(self, transaction_id):
        return '', 204


class AddSale(Resource):
    def post(self):
        return '', 204
