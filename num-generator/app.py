#!flask/bin/python
from flask import Flask, jsonify, make_response
import sys
import requests
from random import randint
app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return "test"

@app.route('/numgen/max/<int:max>/', methods=['GET'])
def num_gen_minmax(max):
    rand = randint(0,max)
    return jsonify({"Random Number":rand})

@app.route('/anEndpoint')
def make_request():
    return requests.get('http://example.com').content

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9017)




