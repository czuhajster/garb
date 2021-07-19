class DateRange(dict):

    def __init__(self, startDate: str, endDate: str):
        """Initialise attributes in format 'YYYY-MM-DD'"""
        self['startDate'] = startDate
        self['endDate'] = endDate
