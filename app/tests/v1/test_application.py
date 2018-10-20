import unittest
from flask import json
from app import create_app


class TestClient(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def teardown(self):
        self.app_context.pop()

    def test_all_products_endpoint(self):
        response = self.client.get('api/v1/products')
        self.assertEqual(response.status_code, 200)

    def test_single_product_endpoint(self):
        response = self.client.get('api/v1/products/1')
        self.assertEqual(response.status_code, 200)

    def test_add_product_endpoint(self):
        response = self.client.post('api/v1/products',
                                    data=json.dumps({
                                        "category": "Mango",
                                        "name": "fruits",
                                        "price": 30
                                    }), content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200)

    def test_update_product_endpoint(self):
        response = self.client.put('api/v1/products/update/2', data=json.dumps({
            "category": "mango",
            "name": "vegetables",
            "price": 15
        }), content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200)

    def test_all_sales_endpoint(self):
        response = self.client.get('api/v1/sales')
        self.assertEqual(response.status_code, 200)

    def test_single_sale_item_endpoint(self):
        response = self.client.get('api/v1/sales/1')
        self.assertEqual(response.status_code, 200)

    def test_add_sales_endpoint(self):
        response = self.client.post('api/v1/sales',
                                    data=json.dumps({
                                        "item": [
                                            {
                                                "product_id": 7,
                                                "quantity": 8,
                                                "unit_price": 10,
                                                "cost": 80
                                            }
                                        ],
                                        "total_cost": 180
                                    }), content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
