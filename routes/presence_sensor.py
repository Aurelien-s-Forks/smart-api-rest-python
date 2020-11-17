from flask import jsonify
from datetime import datetime
import random
from . import routes


@routes.route('/api/presence-sensor/<room_id>', methods=['GET'])
def get_presence(room_id=0):
    room_data = {
        'room_id': room_id,
        'is_there_someone': bool(random.getrandbits(1)),
        'date': datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    }
    return jsonify(room_data)
