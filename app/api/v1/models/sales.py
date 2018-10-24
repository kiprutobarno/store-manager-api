sales = []


class Sale(object):
    def __init__(self):
        self.sales = sales

    def create_sale(self, product_name, quantity, unit_price, category):
        if product_name and quantity and unit_price and category:
            sale = {
                "transaction_id": len(self.sales)+1,
                "product_name": product_name,
                "quantity": quantity,
                "unit_price": unit_price,
                "category": category
            }
            self.sales.append(sale)
            return sale

    def get_specific_sale(self, transaction_id):
        for sale in self.sales:
            if sale['transaction_id'] == transaction_id:
                return sale

    def get_all_sales(self):
        return self.sales
