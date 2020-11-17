from . import entity
from Appartment import *

class Sensor:
    def __init__(self, id, type, unit, appartement):
        self.Id = id
        self.Type = type
        self.Appartment = (Appartment) appartment

    @property
    def Id(self):
        return self.__id
    
    @Id.setter
    def Id(self, id):
        self.__id = id
    
    @property
    def Type(self):
        return self.__type
    
    @Type.setter
    def setType(self, type):
        self.__type = type

    @property
    def Appartment(self):
        return self.__appartment

    @Appartment.setter
    def Appartment(self, appartment):
        self.__appartment = appartment


