import unittest
from flask import Flask, json

app = Flask(__name__)


class TestingEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_to_get_all_sales(self):
        """this test check  all sales """
        response = self.app.get('/api/v1/sales', content_type="application/json")
        self.assertTrue(response.status_code, 200)

    def test_get_specific_sale(self):
        """ this test checks a specific sale transaction """
        response = self.app.get('/api/v1/sales/1', content_type="application/json")
        self.assertTrue(response.status_code, 200)

    def test_error_id(self):
        """this test checks an error in transaction id """
        transaction_id = "1"
        api_url = '/api/v1/sales/' + transaction_id
        response = self.app.get(api_url)
        self.assertRaises(TypeError, response)

    def test_non_existent_transaction_id(self):
        """Test check none existing transaction_id """
        response = self.app.get('/api/v1/sales/20', content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def test_error_when_product_name_not_string(self):
        """Test whether product_name  parameter is a string"""
        response = self.app.post('/api/v1/sales', data=json.dumps({"product_name": 7}),
                                 content_type="application/json", follow_redirects=True)
        self.assertRaises(TypeError, response)

    def test_error_when_email_not_string(self):
        """Test whether product_name  parameter is a string"""
        response = self.app.post('/api/v1/signup', data=json.dumps({"email": 7}),
                                 content_type="application/json", follow_redirects=True)
        self.assertRaises(TypeError, response)

    def test_mandatory_parameter_missing_in_a_sale(self):
        """Test if mandatory parameter product_name is not passed"""
        response = self.app.post('/api/v1/sales', data=json.dumps({"product_name": "Water Melon"}),
                                 content_type="application/json", follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_to_get_all_products(self):
        """These tests check  all products"""
        response = self.app.get('/api/v1/products', content_type="application/json")
        self.assertTrue(response.status_code, 200)

    def test_get_specific_product(self):
        """ this test checks a specific product"""
        response = self.app.get('/api/v1/products/2', content_type="application/json")
        self.assertTrue(response.status_code, 200)

    def test_error_product_id(self):
        """Test to check error in specific product"""
        product_id = "1"
        api_url = '/api/v1/products/' + product_id
        response = self.app.get(api_url)
        self.assertRaises(TypeError, response)

    def test_non_existent_product_id(self):
        """Test check none existing product_id """
        response = self.app.get('/api/v1/products/15', content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def test_error_when_product_is_not_passed(self):
        """Test whether product_name  parameter is a string"""
        response = self.app.post('/api/v1/products', data=json.dumps({"product_name": 17}),
                                 content_type="application/json", follow_redirects=True)
        self.assertRaises(TypeError, response)

    def test_parameter_missing_in_created_product(self):
        """Test if mandatory parameter product_name is not passed"""
        response = self.app.post('/api/v1/products', data=json.dumps({"product_name": "Banana"}),
                                 content_type="application/json", follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def teardown(self):
        pass

