#!flask/bin/python
from flask import Flask, json
from flask_swagger_ui import get_swaggerui_blueprint
from route import *
from entity import *

swaggerui_blueprint = get_swaggerui_blueprint(
    '/api/docs',
    'http://petstore.swagger.io/v2/swagger.json' ,
    config={
        'app_name': "Building AI Systems",
    }
)

app = Flask(__name__)
app.register_blueprint(entity)
app.register_blueprint(swaggerui_blueprint)
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
