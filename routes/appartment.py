from flask import jsonify
from datetime import datetime
import pytz
import random
from . import routes


@routes.route('/api/appartment/<id>', methods=['GET'])
def get_appartment(id=0):
    room_data = {
        'id': id,
    }
    return jsonify(room_data)


@routes.route('/api/appartment/<id>/sensors', methods=['GET'])
def get_appartment_sensors(id=0):
    appartment_data = {
        'appartment_id': id,
        'sensors': [
            {
                'id': 0,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(15, 22),
                    'date': datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S")
                }
            },
            {
                'id': 4,
                'type': 'pipeline-pressure',
                'value': {
                    'pressure': random.randint(1, 5),
                    'date': datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S")
                }
            }
        ]
    }
    return jsonify(appartment_data)