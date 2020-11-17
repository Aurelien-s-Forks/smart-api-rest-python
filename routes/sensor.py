from flask import jsonify
from datetime import datetime
import pytz
import random
from . import routes


@routes.route('/api/sensor/<sensor_id>', methods=['GET'])
def get_sensor(sensor_id=0):
    if int(sensor_id) % 2 == 0:
        room_data = {
            'id': sensor_id,
            'type': 'temperature',
            'value': {
                'temperature': random.randint(15, 22),
                'date': datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S")
            }
        }
    else:
        room_data = {
            'id': sensor_id,
            'type': 'pipeline-pressure',
            'value': {
                'pressure': random.randint(1, 5),
                'date': datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S")
            }
        }
    return jsonify(room_data)
