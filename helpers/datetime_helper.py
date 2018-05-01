"""
date time helper  provides some utility functions to work with date time
"""
from datetime import datetime


class DateTimeHelper:
    """
    Date time helper provides some utility functions to work with date time
    """
    def __init__(self):
        pass

    @staticmethod
    def datetime_from_timestamp(time_stamp: int, time_zone=None):
        """
        returns date time from timestamp
        :param time_stamp: timestamp in UNIX Epoch time format
        :param time_zone: time zone with respect to which to convert time to, default to None
        :return: date time corresponding to timestamp, if input is not correct, returns None
        """
        try:
            return datetime.fromtimestamp(time_stamp, time_zone)
        except ValueError as value_error:
            print(value_error)
        return None

    @staticmethod
    def datetime_formatted(time_stamp: int, format_string='%Y-%m-%d %H:%M:%S'):
        """
        returns date time in a user prescribed format from unix epoch time format
        :param time_stamp: time stamp in unit epoch format
        :param format_string: to which format to convert to
        :return: formatted datetime from unix epoch time
        """
        try:
            return DateTimeHelper.datetime_from_timestamp(time_stamp, None).strftime(format_string)
        except ValueError as value_error:
            print(value_error)
        return None
