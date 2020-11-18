from flask import Blueprint

controller = Blueprint('controller', __name__)

from .ApartmentController import *
from .SensorController import *
