from flask import jsonify
from . import routes
from datetime import datetime
import random
import pytz


@routes.route('/api/apartment/<apartment_id>', methods=['GET'])
def get_apartment(apartment_id=0):
    room_data = {
        'id': apartment_id,
    }
    return jsonify(room_data)


@routes.route('/api/apartment/<apartment_id>/sensors', methods=['GET'])
def get_apartment_sensors(apartment_id=0):
    apartment_data = {
        'apartment_id': apartment_id,
        'sensors': [
            {
                'id': '0',
                'type': 'pipeline-pressure',
                'value': {
                    'pressure': random.randint(1, 5),
                    'date': datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S")
                }
            },
            {
                'id': '5',
                'type': 'temperature',
                'value': {
                    'pressure': random.randint(15, 22),
                    'date': datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S")
                }
            }
        ]
    }
    return jsonify(apartment_data)
