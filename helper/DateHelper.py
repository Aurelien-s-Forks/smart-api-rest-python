from datetime import datetime
import pytz


class DateHelper:
    @staticmethod
    def get_today_date():
        return datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S")
