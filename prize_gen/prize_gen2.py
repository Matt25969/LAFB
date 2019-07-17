from flask import Flask, jsonify, make_response
import random
import requests
from random import randrange
prize_gen = Flask(__name__)


@prize_gen.route('/prize_gen/', methods=['GET'])
def reset(prob=25):
    prize=100
    percent = random.randrange(100)
    if prob > percent:
        request.get('http://52.142.204.121:9000/notify')
        return jsonify({"User has won":prize})
    else:
        return "No prize for you"


if __name__ == '__main__':
     prize_gen.run(host='0.0.0.0', port=5000)
