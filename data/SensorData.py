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
                'sensor_id': 0,
                'type': 'pipeline-pressure',
                'value': {
                    'pressure': random.randint(1, 5),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 0,
                'sensor_id': 1,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(15, 22),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 0,
                'sensor_id': 2,
                'type': 'humidity',
                'value': {
                    'humidity': random.randint(20, 80),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 1,
                'sensor_id': 3,
                'type': 'pipeline-pressure',
                'value': {
                    'pressure': random.randint(1, 5),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 1,
                'sensor_id': 4,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(19, 22),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 1,
                'sensor_id': 5,
                'type': 'humidity',
                'value': {
                    'humidity': random.randint(20, 80),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 2,
                'sensor_id': 6,
                'type': 'pipeline-pressure',
                'value': {
                    'pressure': random.randint(1, 5),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 2,
                'sensor_id': 7,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(15, 25),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 2,
                'sensor_id': 8,
                'type': 'humidity',
                'value': {
                    'humidity': random.randint(40, 80),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 3,
                'sensor_id': 9,
                'type': 'pipeline-pressure',
                'value': {
                    'pressure': random.randint(3, 6),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 3,
                'sensor_id': 10,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(20, 30),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 3,
                'sensor_id': 11,
                'type': 'humidity',
                'value': {
                    'humidity': random.randint(40, 50),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 4,
                'sensor_id': 12,
                'type': 'pipeline-pressure',
                'value': {
                    'pressure': random.randint(1, 5),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 4,
                'sensor_id': 13,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(20, 22),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 4,
                'sensor_id': 14,
                'type': 'humidity',
                'value': {
                    'humidity': random.randint(30, 60),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 5,
                'sensor_id': 15,
                'type': 'pipeline-pressure',
                'value': {
                    'pressure': random.randint(1, 5),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 5,
                'sensor_id': 16,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(10, 22),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 5,
                'sensor_id': 17,
                'type': 'humidity',
                'value': {
                    'humidity': random.randint(20, 50),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 6,
                'sensor_id': 18,
                'type': 'pipeline-pressure',
                'value': {
                    'pressure': random.randint(1, 5),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 6,
                'sensor_id': 19,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(15, 30),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 6,
                'sensor_id': 20,
                'type': 'humidity',
                'value': {
                    'humidity': random.randint(50, 80),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 7,
                'sensor_id': 21,
                'type': 'pipeline-pressure',
                'value': {
                    'pressure': random.randint(1, 5),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 7,
                'sensor_id': 22,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(15, 22),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 7,
                'sensor_id': 23,
                'type': 'humidity',
                'value': {
                    'humidity': random.randint(20, 80),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 8,
                'sensor_id': 24,
                'type': 'pipeline-pressure',
                'value': {
                    'pressure': random.randint(1, 5),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 8,
                'sensor_id': 25,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(15, 22),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 8,
                'sensor_id': 26,
                'type': 'humidity',
                'value': {
                    'humidity': random.randint(20, 80),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 9,
                'sensor_id': 27,
                'type': 'pipeline-pressure',
                'value': {
                    'pressure': random.randint(1, 5),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 9,
                'sensor_id': 28,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(15, 22),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 9,
                'sensor_id': 29,
                'type': 'humidity',
                'value': {
                    'humidity': random.randint(20, 80),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 10,
                'sensor_id': 30,
                'type': 'pipeline-pressure',
                'value': {
                    'pressure': random.randint(1, 2),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 10,
                'sensor_id': 31,
                'type': 'temperature',
                'value': {
                    'temperature': random.randint(14, 25),
                    'date': DateHelper.get_today_date()
                }
            },
            {
                'apartment_id': 10,
                'sensor_id': 32,
                'type': 'humidity',
                'value': {
                    'humidity': random.randint(70, 80),
                    'date': DateHelper.get_today_date()
                }
            }
        ]
        return sensor_data

    @staticmethod
    def get_by_id(sensor_id=0):
        return next(x for x in SensorData.get_all() if x["sensor_id"] == int(sensor_id))
