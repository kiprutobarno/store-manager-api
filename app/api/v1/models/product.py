class Product(object):
    products = []

    def __init__(self, product_name, quantity, unit_price, category):
        self.product_id = len(Product.products)+1
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price
        self.category = category

    def add_product(self):
        product = dict(
            product_id=self.product_id,
            product_name=self.product_name,
            quantity=self.quantity,
            unit_price=self.unit_price,
            category=self.category
        )
        Product.products.append(product)
        return product

    @staticmethod
    def get_specific_product(product_id):
        for product in Product.products:
            if product['product_id'] == product_id:
                return product

    @staticmethod
    def get_all_products():
        return Product.products


