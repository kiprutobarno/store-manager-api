from flask import Blueprint
from flask_restful import Api


from v1.views.products import Product, SpecificProduct
from v1.views.sales import SaleTransaction, SpecificSale
from v1.views.users import Registration, Login, Tokens
from v1.views.landing import LandingPage


# create blueprint
v1_blueprint = Blueprint('api_v1', __name__, url_prefix="/api/v1")
api_v1 = Api(v1_blueprint)

api_v1.add_resource(LandingPage, '/')
api_v1.add_resource(Product, '/products')
api_v1.add_resource(SpecificProduct, '/products/<int:product_id>')
api_v1.add_resource(SaleTransaction, '/sales')
api_v1.add_resource(SpecificSale, '/sales/<int:transaction_id>')
api_v1.add_resource(Tokens, '/tokens')


api_v1.add_resource(Registration, '/register')
api_v1.add_resource(Login, '/login')

