from flask import Flask
app = Flask(__name__)

import datetime


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/time')
def time():
    ts = datetime.datetime.now()
    return ts.strftime("%Y-%m-%d %H:%M:%S")


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
