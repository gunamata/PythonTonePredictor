#!flask/bin/python
from flask import Flask
import random

app = Flask(__name__)

@app.route('/tone')
def toneEstimator():
    tones = ["humerous","ironic","cynical"];
    return random.choice(tones)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)