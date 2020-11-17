import json


class Apartment:
    def __init__(self, numero, sensors):
        self.numero = numero
        self.sensors = sensors

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, val):
        self.__numero = val

    @property
    def sensors(self):
        return self.__sensors

    @sensors.setter
    def sensors(self, val):
        self.__sensors = val

    def toJSON(self):
        return json.dumps(self)