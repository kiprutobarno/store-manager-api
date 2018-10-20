# store-manager-api
Store Manager API 

TravisCI Test


[![Build Status](https://travis-ci.com/kipruto/store-manager-api.svg?branch=ch-automated-api-endpoint-tests-travis-161361514)](https://travis-ci.com/kipruto/store-manager-api)



Coverall Test


[![Coverage Status](https://coveralls.io/repos/github/kipruto/store-manager-api/badge.svg?branch=master)](https://coveralls.io/github/kipruto/store-manager-api?branch=master)


USING STORE MANAGER API
================================


1. Requirements
===============================

i. Postman
ii. An internet connection

OBTAINING AUTHENTICATION TOKENS
=================================
1. Using postman POST, enter the URL https://floating-hollows-10589.herokuapp.com/auth and press send, the Authentication token wil pop up in the form below. Copy it without quotes the opening and closing quotes

USING THE AUTHENTICATION TOKENS
==================================
1. After choosing your request method and inputting your URL, in postman Headers section of postman's input, choose KEY as Authorization and VALUE as JWT <paste your previously copied token>
2. Press enter
  
 CONSUMING THE API
 =================
 
 1. View Sales: GET https://floating-hollows-10589.herokuapp.com/api/v1/sales
 2. View a specific sale order GET https://floating-hollows-10589.herokuapp.com/api/v1/sales/<transaction_id>
 3. View Products: GET https://floating-hollows-10589.herokuapp.com/api/v1/products
 4. Viewing a specific product GET https://floating-hollows-10589.herokuapp.com/api/v1/products/<product_id>
 5. Update Products: POST https://floating-hollows-10589.herokuapp.com/update/api/v1/products/<product_id>
 4. Add Products: POST https://floating-hollows-10589.herokuapp.com/api/v1/products/
 6: Add Sales: POST https://floating-hollows-10589.herokuapp.com/api/v1/sales
