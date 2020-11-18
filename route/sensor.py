from flask import jsonify
from . import routes
from data import SensorData


@routes.route('/api/sensor', methods=['GET'])
def get_sensors():
    return jsonify(SensorData.get_all())


@routes.route('/api/sensor/<sensor_id>', methods=['GET'])
def get_sensor(sensor_id=0):
    return jsonify(SensorData.get_by_id(sensor_id))
