from flask import Blueprint

routes = Blueprint('route', __name__)

from .apartment import *
from .sensor import *
