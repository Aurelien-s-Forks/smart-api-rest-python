from flask import Blueprint

routes = Blueprint('routes', __name__)

from .pipeline_pressure import *
from .temperature import *
