from flask import json
from datetime import datetime
import random
from . import routes


@routes.route('/api/pipeline-pressure/<room_id>', methods=['GET'])
def get_pipeline_pressure(room_id=0):
    return "Hello pipeline"
