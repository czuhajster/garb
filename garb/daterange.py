"""DateRange module

This module defines the DateRange object.
"""

class DateRange(dict):
    """An object representing a date range.

    DateRange object uses date in ISO format 'YYYY-MM-DD'.
    """

    def __init__(self, start_date: str, end_date: str):
        """Initialises a DateRange object.
        """
        self['startDate'] = start_date
        self['endDate'] = end_date
