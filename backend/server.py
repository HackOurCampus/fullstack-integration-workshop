import time
from flask import Flask

app = Flask(__name__)

PRODUCTS = [
  { 'category': 'Sporting Goods', 'price': '$49.99', 'stocked': True, 'name': 'Football' },
  { 'category': 'Sporting Goods', 'price': '$9.99', 'stocked': True, 'name': 'Baseball' },
  { 'category': 'Sporting Goods', 'price': '$29.99', 'stocked': False, 'name': 'Basketball' },
  { 'category': 'Electronics', 'price': '$999.99', 'stocked': True, 'name': 'iPad Pro' },
  { 'category': 'Electronics', 'price': '$399.99', 'stocked': False, 'name': 'iPhone 5' },
  { 'category': 'Electronics', 'price': '$199.99', 'stocked': True, 'name': 'Nexus 7' }
]

@app.route('/products')
def get_all_products():
    return {'products': PRODUCTS}
