"""Cohort module

This module defines cohort-relates objects: Type, Cohort, CohortGroup.
"""

from enum import Enum

from .daterange import DateRange

class Type(Enum):
    """A Type object.
    """

    FIRST_VISIT_DATE = "FIRST_VISIT_DATE",
    UNSPECIFIED_COHORT_TYPE = "FIRST_VISIT_DATE"

class Cohort (dict):
    """A Cohort object.
    """

    def __init__(self,
                 name: str,
                 type: Type =Type.UNSPECIFIED_COHORT_TYPE,
                 dateRange: DateRange =None
    ) -> None:
        """Initialises a Cohort object.
        """
        self['name'] = name
        self['type'] = type
        self['dateRange'] = dateRange

class CohortGroup (dict):
    """A CohortGroup object.
    """
    
    def __init__(self,
                 cohorts: list[Cohort],
                 lifetimeValue: bool
    ) -> None:
        """Initialises a CohortGroup object.
        """
        self['cohorts'] = cohorts
        self['lifetimeValue'] = lifetimeValue

