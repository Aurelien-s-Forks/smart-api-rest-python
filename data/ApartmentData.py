import random
from helper import DateHelper


class ApartmentData:
    def __init__(self):
        pass

    @staticmethod
    def get_all():
        apartment_data = [
            {
                'apartment_id': 0,
                'sensors': [
                    {
                        'sensor_id': 3,
                        'type': 'pipeline-pressure',
                        'value': {
                            'pressure': random.randint(1, 5),
                            'date': DateHelper.get_today_date()
                        }
                    },
                    {
                        'sensor_id': 7,
                        'type': 'temperature',
                        'value': {
                            'pressure': random.randint(15, 22),
                            'date': DateHelper.get_today_date()
                        }
                    }
                ]
            },
            {
                'apartment_id': 1,
                'sensors': [
                    {
                        'sensor_id': 2,
                        'type': 'temperature',
                        'value': {
                            'pressure': random.randint(15, 22),
                            'date': DateHelper.get_today_date()
                        }
                    }
                ]
            },
            {
                'apartment_id': 2,
                'sensors': [
                    {
                        'sensor_id': 8,
                        'type': 'temperature',
                        'value': {
                            'pressure': random.randint(10, 15),
                            'date': DateHelper.get_today_date()
                        }
                    }
                ]
            }
        ]
        return apartment_data

    @staticmethod
    def get_by_id(apartment_id=0):
        return next(x for x in ApartmentData.get_all() if x["apartment_id"] == int(apartment_id))
