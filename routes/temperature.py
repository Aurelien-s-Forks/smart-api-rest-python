from flask import json
from datetime import datetime
import random
from . import routes


@routes.route('/api/temperature/<room_id>', methods=['GET'])
def get_temperature(room_id=0):
    return "Hello temperature"
