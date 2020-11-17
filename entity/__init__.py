from flask import Blueprint

routes = Blueprint('Entity', __name__)

from .Apartment import *
from .Sensor import *
