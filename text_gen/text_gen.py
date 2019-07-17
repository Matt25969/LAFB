from flask import Flask, jsonify, make_response
import random
import string
text_gen = Flask(__name__)


@text_gen.route('/text_gen/', methods=['GET'])
def text_gen_method():
    rand = random.choice(string.ascii_lowercase)
    return jsonify({"Random string":rand})

if __name__ == '__main__':
     text_gen.run(host='0.0.0.0', port=9017)
