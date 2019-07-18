#!flask/bin/python
from flask import Flask, jsonify, make_response
import os
import sys
import requests
import random
import string
from random import randint
from flask import request
app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    return "test"


@app.route('/prize', methods=['POST'])
def prize():
    data = request.data
    return data


@app.route('/anEndpoint')
def make_request():
    return requests.get('http://example.com').content


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 50003))
    app.run(host='0.0.0.0', port=port)
