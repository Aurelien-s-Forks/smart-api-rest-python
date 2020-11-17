from flask import jsonify
from . import routes


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
                'id': 0
            },
            {
                'id': 4
            }
        ]
    }
    return jsonify(apartment_data)
