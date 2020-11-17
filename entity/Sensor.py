from entity import Apartment, Model


class Sensor:
    def __init__(self, id, model, unit, apartement, values):
        self.id = id
        self.model = model
        self.unit = unit
        self.apartment = apartement
        self.values = values

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, val):
        self.__id = val
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, val):
        if type(val) == Model:
            self.__model = val

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, val):
        self.__unit = val

    @property
    def apartment(self):
        return self.__appartment

    @apartment.setter
    def apartment(self, apartment):
        if type(apartment) == Apartment:
            self.__appartment = apartment

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, val):
        self.__values = val


