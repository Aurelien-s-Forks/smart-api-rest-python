from flask import jsonify
from datetime import datetime
import random
from . import routes


@routes.route('/api/pipeline-pressure/<room_id>', methods=['GET'])
def get_pipeline_pressure(room_id=0):
    room_data = {
        'room_id': room_id,
        'pipeline_pressure': random.randint(1, 5),
        'date': datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    }
    return jsonify(room_data)
