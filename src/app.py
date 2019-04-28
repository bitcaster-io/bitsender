import os
from pathlib import Path

from flask import Flask
from flask import render_template

here = Path(__file__).parent

app = Flask(__name__)


@app.route('/')
def home():
    resp = render_template('index.html')
    resp.headers['server'] = os.environ.get('SERVER_NAME')

    return resp
    # return render_template(str(Path(here / 'templates/index.html')))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
