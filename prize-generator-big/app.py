#!flask/bin/python
from flask import Flask, jsonify, make_response
import sys
import requests
import random
import json
import string
import urllib2
from random import randint
app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    return "test"


@app.route('/prize/', methods=['POST'])
def prize():

    data = request.data
    req_data = {}
    req_data['firstName'] = data.get('firstName', '')
    req_data['lastName'] = data.get('lastName', '')
    req_data['accountnumber'] = data.get('accountnumber', '')
    winners = random.randint(1, 100)
    award = random.randint(1, 10)

    if winners > 75:
        req_data['prize'] = str(award*500)
        prize = requests.get('http://example.com/notify').content
        print(prize)
    elif winners > 50:
        req_data['prize'] = str(award*100)
        prize = requests.get('http://example.com/notify').content
        print(prize)
    else:
        req_data['prize'] = "0"
    req_data = json.dumps(req_data)
    return requests.post('http://example.com/createAccount', json=req_data)


@app.route('/anEndpoint')
def make_request():
    return requests.get('http://example.com').content


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9017)
