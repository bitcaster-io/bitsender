import os
from pathlib import Path

from flask import Flask
from flask import render_template

here = Path(__file__).parent

app = Flask(__name__)


@app.route('/')
def index():
    resp = render_template('index.html')
    return resp


@app.route('/<page>/')
def editor(page):
    if page in ['message', 'params']:
        resp = render_template('%s.html' % page, page=page)
        return resp
    return "", 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
