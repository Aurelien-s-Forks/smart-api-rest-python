from flask import Blueprint

routes = Blueprint('Entity', __name__)

from .Appartment import *
from .Sensor import *
