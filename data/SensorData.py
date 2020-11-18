import random
from helper import DateHelper


class SensorData:
    def __init__(self):
        pass

    @staticmethod
    def get_all():
        sensor_data = [
            {
                'apartment_id': 0,
                'sensor_id': 3,
                'type': 'pipeline-pressure',
                'value': {
                    'pressure': random.randint(1, 5),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 0,
                'sensor_id': 7,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(15, 22),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 1,
                'sensor_id': 2,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(15, 22),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 2,
                'sensor_id': 8,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(10, 15),
                    'date': DateHelper.get_today_date()
                }
            }
        ]
        return sensor_data

    @staticmethod
    def get_by_id(sensor_id=0):
        return next(x for x in SensorData.get_all() if x["sensor_id"] == int(sensor_id))
