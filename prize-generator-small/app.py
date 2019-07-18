#!flask/bin/python
from flask import Flask, jsonify, make_response
import sys
import requests
import random
import string
from random import randint
import urllib2
app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    return "test"


@app.route('/prize/', methods=['GET'])
def prize():
    req_data = {}
    req_data['firstname'] = 'Bert'
    req_data['lastname'] = 'Smith'
    winners = random.randint(1, 100)
    award = random.randint(1, 10)

    if winners > 75:
        req_data['prize'] = str(award*100)
    elif winners > 50:
        req_data['prize'] = str(award*10)
    else:
        req_data['prize'] = "0"
    req_data = json.dumps(req_data)
    requests.post('http://example.com', data=req_data)
    contents = urllib2.urlopen("http://example.com/notify").read()
    print(contents)
    return req_data


@app.route('/anEndpoint')
def make_request():
    return requests.get('http://example.com').content


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9017)
