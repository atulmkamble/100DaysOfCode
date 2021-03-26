"""
This program implements a basic Flask app
"""

from flask import Flask
import random

app = Flask(__name__)

print(__name__)
print(random.__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def say_bye():
    return 'Bye Bye'


if __name__ == '__main__':
    app.run()
