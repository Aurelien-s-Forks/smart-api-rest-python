from flask import jsonify
from . import controller
from data import ApartmentData


@controller.route('/api/apartment/<apartment_id>', methods=['GET'])
def get_apartment(apartment_id=0):
    return jsonify(ApartmentData.get_all())


@controller.route('/api/apartment/<apartment_id>/sensors', methods=['GET'])
def get_apartment_sensors(apartment_id=0):
    return jsonify(ApartmentData.get_all())
