from flask import Blueprint
from flask_restful import Api

from v1.views.users import SignUp, Login
from v1.views.products import Products, GetSpecificProduct
from v1.views.sales import Sales, GetSpecificSale


# create blueprint
v1_blueprint = Blueprint('api_v1', __name__, url_prefix="/api/v1")
api_v1 = Api(v1_blueprint)

api_v1.add_resource(SignUp, '/signup')
api_v1.add_resource(Login, '/login')
api_v1.add_resource(Products, '/products')
api_v1.add_resource(GetSpecificProduct, '/products/<int:product_id>')
api_v1.add_resource(Sales, '/sales')
api_v1.add_resource(GetSpecificSale, '/sales/<int:transaction_id>')
