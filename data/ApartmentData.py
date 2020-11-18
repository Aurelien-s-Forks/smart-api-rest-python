from datetime import datetime
import random
import pytz


class ApartmentData:
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
                            'date': datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S")
                        }
                    },
                    {
                        'sensor_id': 7,
                        'type': 'temperature',
                        'value': {
                            'pressure': random.randint(15, 22),
                            'date': datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S")
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
                            'date': datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S")
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
                            'date': datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S")
                        }
                    }
                ]
            }
        ]
        return apartment_data


