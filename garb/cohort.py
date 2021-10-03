from enum import Enum

from .daterange import DateRange

class Type(Enum):
    FIRST_VISIT_DATE = "FIRST_VISIT_DATE",
    UNSPECIFIED_COHORT_TYPE = "FIRST_VISIT_DATE"

class Cohort (dict):

    def __init__(self,
                 name: str,
                 type: Type =Type.UNSPECIFIED_COHORT_TYPE,
                 dateRange: DateRange =None):
        self['name'] = name
        self['type'] = type
        self['dateRange'] = dateRange

class CohortGroup (dict):
    
    def __init__(self,
                 cohorts: list[Cohort],
                 lifetimeValue: bool):
        self['cohorts'] = cohorts
        self['lifetimeValue'] = lifetimeValue

