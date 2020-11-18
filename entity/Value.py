import datetime
from . import entity


class Value:
    def __init__(self, date, value, sensor):
        self.date = date
        self.value = value
        self.sensor = sensor

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, val):
        if type(val) == datetime:
            self.__date = val

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    @property
    def sensor(self):
        return self.__sensor

    @sensor.setter
    def sensor(self, val):
        if type(val) == Sensor:
            self.__sensor = val
