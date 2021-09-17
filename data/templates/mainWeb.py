from static.functions import *
from static.classes import *

from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok


app = Flask(__name__)
run_with_ngrok(app)


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()