from flask import Blueprint
from flask_restful import Api
from .v1.views.products import Product, SpecificProduct
from .v1.views.sales import Sale, SpecificSale
from .v1.views.users import Registration, Login
v1_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(v1_blueprint)

api.add_resource(Product, '/products')
api.add_resource(SpecificProduct, '/products/<productID>')
api.add_resource(Sale, '/sales')
api.add_resource(SpecificSale, '/sales/<saleID>')
api.add_resource(Registration, '/auth/signup')
api.add_resource(Login, '/auth/login')

