from flask import jsonify
from datetime import datetime
import pytz
import random
from . import routes


@routes.route('/api/apartment/<id>', methods=['GET'])
def get_apartment(id=0):
    room_data = {
        'id': id,
    }
    return jsonify(room_data)


@routes.route('/api/apartment/<id>/sensors', methods=['GET'])
def get_apartment_sensors(id=0):
    apartment_data = {
        'apartment_id': id,
        'sensors': [
            {
                'id': 0
            },
            {
                'id': 4
            }
        ]
    }
    return jsonify(apartment_data)