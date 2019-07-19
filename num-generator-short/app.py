#!flask/bin/python
from flask import Flask, jsonify, make_response
import os
import sys
import requests
import random
import string
from random import randint
app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    return "test"


@app.route('/numGen/', methods=['GET'])
def numGen():
    numbers = ''
    for x in range(6):
        numbers += str(random.randint(0, 9))
    return numbers


@app.route('/anEndpoint')
def make_request():
    return requests.get('http://example.com').content


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 50002))
    app.run(host='0.0.0.0', port=port)
