from flask import Blueprint

routes = Blueprint('routes', __name__)

from .apartment import *
from .sensor import *
