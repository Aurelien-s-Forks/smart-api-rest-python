from flask import jsonify
from . import controller
from data import SensorData


@controller.route('/api/sensors', methods=['GET'])
def get_sensors():
    return jsonify(SensorData.get_all())


@controller.route('/api/sensor/<sensor_id>', methods=['GET'])
def get_sensor(sensor_id=0):
    return jsonify(SensorData.get_by_id(int(sensor_id)))
