import json

from . import entity, Sensor


class Apartment:
    def __init__(self, number, sensors=None):
        if sensors is None:
            sensors = []
        self.number = number
        self.sensors = sensors

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, val):
        self.__number = val

    @property
    def sensors(self):
        return self.__sensors

    @sensors.setter
    def sensors(self, val):
        self.__sensors = val

    def addSensor(self, val):
        if type(val) == Sensor:
            self.sensors.append(val)

    def removeSensor(self, val):
        if type(val) == Sensor:
            self.sensors.append(val)

    def jsonSensor(self):
        tab = []
        for sensor in self.sensors:
            tab.append(sensor.toJson())

        print(tab)
        return tab

    def toJSON(self):
        return {
            "number": self.number,
            "sensors": self.jsonSensor()
        }


