"""DateRange module

This module defines the DateRange object.
"""

class DateRange(dict):
    """A DateRange object.

    DateRange object uses date in format 'YYYY-MM-DD'.
    """

    def __init__(self, startDate: str, endDate: str):
        """Initialises a DateRange object.
        """
        self['startDate'] = startDate
        self['endDate'] = endDate
