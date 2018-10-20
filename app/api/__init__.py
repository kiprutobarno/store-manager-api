from flask import Blueprint
from flask_restful import Api


from v1.products import ShowAllProducts, ShowSingleProduct, AddProduct, UpdateProduct, DeleteProduct
from v1.sales import ShowAllSales, ShowSingleSale, AddSale

# create blueprint
v1_blueprint = Blueprint('api_v1', __name__, url_prefix="/api/v1")
api_v1 = Api(v1_blueprint)

# create endpoints

# products endpoints

api_v1.add_resource(ShowAllProducts, '/products')
api_v1.add_resource(ShowSingleProduct, '/products/<int:product_id>')
api_v1.add_resource(AddProduct, '/products')
api_v1.add_resource(UpdateProduct, '/products/update/<int:product_id>')
api_v1.add_resource(DeleteProduct, '/products/delete/<int:product_id>')
# sales endpoints
api_v1.add_resource(ShowAllSales, '/sales')
api_v1.add_resource(ShowSingleSale, '/sales/<int:transaction_id>')
api_v1.add_resource(AddSale, '/sales')
