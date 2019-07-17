import os
import random
from flask import Flask
app = Flask(__name__)

@app.route("/number_generator")
def number():
	print(random(6))
