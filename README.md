# store-manager-api
Store Manager API 

TravisCI Test


[![Build Status](https://travis-ci.com/kipruto/store-manager-api.svg?branch=ch-automated-api-endpoint-tests-travis-161361514)](https://travis-ci.com/kipruto/store-manager-api)



Coverall Test

[![Coverage Status](https://coveralls.io/repos/github/kipruto/store-manager-api/badge.svg?branch=master)](https://coveralls.io/github/kipruto/store-manager-api?branch=master)


USING STORE MANAGER API
================================


Requirements
===============================

1. Postman
2. An internet connection

Generating Authentication Tokens
=================================
1. Using postman POST, enter the URL https://floating-hollows-10589.herokuapp.com/auth and press send, the Authentication token wil pop up in the form below. Copy it without the opening and closing quotes

Using the Authentication Tokens
==================================
1. After choosing your request method and inputting your API URL, in postman Headers section of postman's input, choose KEY as Authorization and VALUE starting with JWT followed by your previously copied token(e.g JWT r4Tf6dGlkh4bgWdhgU1pH.....)
2. Press enter
  
 Consuming the API
 =================
 
 1. View all sales: GET https://floating-hollows-10589.herokuapp.com/api/v1/sales
 2. View a specific sale order GET https://floating-hollows-10589.herokuapp.com/api/v1/sales/<transaction_id>
 3. View all products: GET https://floating-hollows-10589.herokuapp.com/api/v1/products
 4. Viewing a specific product GET https://floating-hollows-10589.herokuapp.com/api/v1/products/<product_id>
 5. Update a specific products: POST https://floating-hollows-10589.herokuapp.com/update/api/v1/products/<product_id>
 6. Add a product: POST https://floating-hollows-10589.herokuapp.com/api/v1/products
 
 7: Add a sale: POST https://floating-hollows-10589.herokuapp.com/api/v1/sales
