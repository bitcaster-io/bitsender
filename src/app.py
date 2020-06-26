import os
from pathlib import Path

from flask import Flask, safe_join
from flask import render_template, send_from_directory

here = Path(__file__).parent

app = Flask(__name__)


@app.route('/')
def index():
    resp = render_template('index.html')
    return resp


@app.route('/p/<path:page>')
def editor(page):
    return render_template(page, page=page)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
