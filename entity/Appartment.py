from . import entity
from Sensor import *
import json

class Appartment:
    def __init__(self, numero, sensors = []):
        self.Numero = numero
        self.Sensors = sensors

    @property
    def Numero(self):
        return self.__Numero

    @Numero.setter
    def Numero(self, val):
        self.__Numero = val

    @property
    def Sensors(self):
        return self.__Sensors

    def toJSON(self):
        return json.dumps(self)