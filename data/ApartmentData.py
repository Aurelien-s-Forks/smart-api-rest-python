from datetime import datetime
import random
import pytz


class ApartmentData:
    @staticmethod
    def get_all():
        apartment_data = {
            'apartment_id': random.randint(0, 9999),
            'sensors': [
                {
                    'id': random.randint(0, 9999),
                    'type': 'pipeline-pressure',
                    'value': {
                        'pressure': random.randint(1, 5),
                        'date': datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S")
                    }
                },
                {
                    'id': random.randint(0, 9999),
                    'type': 'temperature',
                    'value': {
                        'pressure': random.randint(15, 22),
                        'date': datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S")
                    }
                }
            ]
        }
        return apartment_data


