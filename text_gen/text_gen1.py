from flask import Flask, jsonify, make_response
import random
import string

text_gen = Flask(__name__)


@text_gen.route('/text_gen/')
def text_gen_method():
    rand = (''.join(random.choice(string.ascii_lowercase) for i in range(3)))
    return rand

if __name__ == '__main__':
     text_gen.run(host='0.0.0.0', port=9017)
