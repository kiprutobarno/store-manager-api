inventories = []


class Inventory(object):
    def __init__(self):
        self.products = inventories

    def add_product(self, product_name, quantity, unit_price, category):
        product = {
            "product_id": len(self.products)+1,
            "product_name": product_name,
            "quantity": quantity,
            "unit_price": unit_price,
            "category": category
        }
        self.products.append(product)
        return product

    def get_specific_product(self, product_id):
        for product in self.products:
            if product['product_id'] == product_id:
                return product

    def get_all_products(self):
        return self.products
