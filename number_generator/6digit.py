import os
import random
from random import randint
from flask import Flask
app = Flask(__name__)

@app.route("/number_generator")
def number():
	a = randint(0, 999999)
	return a
