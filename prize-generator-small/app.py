#!flask/bin/python
from flask import Flask, jsonify, make_response
import os
import sys
import requests
import random
import string
import json
from random import randint
from flask import request
app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    return "test"


@app.route('/prize', methods=['POST'])
def prize():
    data = request.data
    json.dumps(request.data)
#    data[0]['prize'] = 'winner'
#    req_data = json.loads(data)
#    data.get('firstName','')
#    req_data = {}
#    req_data['lastName'] = 'smith'
#    req_data['accountnumber'] = data.get('accountnumber','')
#    if winners > 75:
#        req_data['prize'] = str(award*100)
#        prize = requests.get('http://example.com/notify').content
#    elif winners > 50:
#        req_data['prize'] = str(award*10)
#        prize = requests.get('http://example.com/notify').content
#    else:
#        req_data['prize'] = "0"
#    req_data = json.dumps(req_data)
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
