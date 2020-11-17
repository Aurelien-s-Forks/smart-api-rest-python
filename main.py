#!flask/bin/python
from flask import Flask, json, jsonify
from datetime import datetime
import random

app = Flask(__name__)


@app.route('/api/')
def index():
    response = app.response_class(
        response=json.dumps("Building AI Systems API"),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/api/pipeline-pressure/<room_id>')
def get_pipeline_pressure(room_id=0):
    room_data = {
        'room_id': room_id,
        'pipeline_pressure': random.randint(1, 5),
        'date': datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    }
    response = app.response_class(
        response=json.dumps(room_data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
