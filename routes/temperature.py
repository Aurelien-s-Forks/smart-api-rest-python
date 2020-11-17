from flask import jsonify
from datetime import datetime
import random
from . import routes


@routes.route('/api/temperature/<room_id>', methods=['GET'])
def get_temperature(room_id=0):
    room_data = {
        'room_id': room_id,
        'temperature': random.randint(15, 22),
        'date': datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    }
    return jsonify(room_data)
