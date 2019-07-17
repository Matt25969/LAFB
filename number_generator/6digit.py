import os
import random
from random import randint
from flask import Flask
app = Flask(__name__)

@app.route("/number_generator")
def number():
	num = randint(100000, 999999)
	return num
