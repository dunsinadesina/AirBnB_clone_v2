#!/usr/bin/python3
"""Starts flask application

the application listens on 0.0.0.0, port 5000
Routes:
	/: displays 'Hello HBNB!'
	/hbnb: displays 'HBNB'
	/c/<text>: displays 'C' followed by the value f <text>
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
	"""Displays 'Hello HBNB!'"""
	return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
	"""displays 'HBNB'"""
	return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
	"""displays 'C' followed by the value of <text>"""
	text = text.replace("_", " ")
	return "C {}".format(text)

if __name__ == "__main__":
	app.run(host="0.0.0.0")
