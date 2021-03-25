from flask import Flask, jsonify, make_response
from random import randint
num_gen = Flask(__name__)

@num_gen.route('/num_gen/')
def num_gen_method():
    rand = randint(100000,999999)
    return str(rand)

if __name__ == '__main__':
     num_gen.run(host='0.0.0.0', port=9018)
