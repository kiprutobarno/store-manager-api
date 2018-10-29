class Sale(object):
    sales = []

    def __init__(self, product_name, quantity, category, unit_price):
        self.transaction_id = len(Sale.sales) + 1
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price
        self.category = category

    def make_sale(self):
        sale = dict(
            transaction_id=self.transaction_id,
            product_name=self.product_name,
            quantity=self.quantity,
            unit_price=self.unit_price,
            category=self.category
        )
        Sale.sales.append(sale)
        return sale

    @staticmethod
    def get_all_sales():
        return Sale.sales

    @staticmethod
    def get_specific_sale(transaction_id):
        for sale in Sale.sales:
            if sale['transaction_id'] == transaction_id:
                return sale
