import requests

from datetime import datetime
from timetools.timeutil import TimeUtil


class PositionUtil:

    @staticmethod
    def testDependency():
        current = datetime.now()
        return TimeUtil.get_start_of_date(current)

    @staticmethod
    def is_coordinate_in_china(latitude, longitude):
        china_latitude_range = (3.86, 53.55)
        china_longitude_range = (73.66, 135.05)

        if china_latitude_range[0] <= latitude <= china_latitude_range[1] and \
                china_longitude_range[0] <= longitude <= china_longitude_range[1]:
            return True
        else:
            return False
