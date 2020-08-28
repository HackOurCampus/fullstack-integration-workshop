import time
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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
    return jsonify({'products': PRODUCTS})

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=8080)