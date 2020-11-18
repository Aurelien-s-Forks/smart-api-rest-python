from flask import Blueprint

data = Blueprint('data', __name__)

from .ApartmentData import ApartmentData
