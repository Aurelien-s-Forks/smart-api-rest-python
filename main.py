#!flask/bin/python
from flask import Flask, json, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    response = app.response_class(
        response=json.dumps("Hello World"),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
