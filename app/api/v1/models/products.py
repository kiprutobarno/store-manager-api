products = []


class Product:
    def __init__(self, data):
        self.product_name = data['product_name']
        self.category = data['category']
        self.quantity = data['quantity']
        self.unit_price = data['unit_price']
        self.inventory = data['inventory']

    def create_product(self):
        product_id = len(products) + 1
        product = {
            'product_id': product_id,
            'product_name': self.product_name,
            'category': self.category,
            'quantity': self.quantity,
            'unit_price': self.unit_price,
            'inventory': self.inventory
            }
        products.append(product)


