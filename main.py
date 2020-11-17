#!flask/bin/python
from flask import Flask

from routes import *

app = Flask(__name__)
app.register_blueprint(routes)


@app.route('/api/', methods=['GET'])
def index():
    response = app.response_class(
        response=json.dumps("Building AI Systems API"),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
