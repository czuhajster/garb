"""Segment Module

This module defines segment-related objects: SegmentDimensionFilterOperator,
SegmentDimensionFilter, SegmentMetricFilterOperator, Scope, SegmentMetricFilter,
SegmentFilterClause, SegmentSequenceStep, SequenceSegment, SegmentFilter,
SegmentDefinition, and Segment.
"""

from enum import Enum
from typing import Union

class SegmentDimensionFilterOperator(Enum):
    """A SegmentDimensionFilterOperator object.
    """

    REGEXP = "REGEXP",
    BEGINS_WITH = "BEGINS_WITH",
    ENDS_WITH = "ENDS_WITH",
    PARTIAL = "PARTIAL",
    EXACT = "EXACT",
    IN_LIST = "IN_LIST",
    NUMERIC_LESS_THAN = "NUMERIC_LESS_THAN",
    NUMERIC_GREATER_THAN = "NUMERIC_GREATER_THAN",
    NUMERIC_BETWEEN = "NUMERIC_BETWEEN",
    OPERATOR_UNSPECIFIED = "REGEXP"

class SegmentDimensionFilter (dict):
    """A SegmentDimensionFilter object.
    """

    def __init__(self,
                 dimensionName: str,
                 operator: SegmentDimensionFilterOperator =SegmentDimensionFilterOperator.OPERATOR_UNSPECIFIED,
                 caseSensitive: bool =False,
                 expressions: list[str] =None,
                 minComparisonValue: str =None,
                 maxComparisonValue: str =None,
    ) -> None:
        """Initialises a SegmentDimensionFilter object.
        """
        self['dimensionName'] = dimensionName
        self['operator'] = operator
        self['caseSensitive'] = caseSensitive
        self['expressions'] = expressions
        self['minComparisonValue'] = minComparisonValue
        self['maxComparisonValue'] = maxComparisonValue

class SegmentMetricFilterOperator (Enum):
    """A SegmentMetricFilterOperator object.
    """

    LESS_THAN = "LESS_THAN",
    GREATER_THAN = "GREATER_THAN",
    EQUAL = "EQUAL",
    BETWEEN = "BETWEEN"
    UNSPECIFIED_OPERATOR = "LESS_THAN"

class Scope (Enum):
    """A Scope object
    """

    PRODUCT = "PRODUCT",
    HIT = "HIT",
    SESSION = "SESSION",
    USER = "USER"
    # TODO: implement `UNSPECIFIED_SCOPE` to default either to `USER` or
    # `SESSION`.

class SegmentMetricFilter (dict):
    """A SegmentMetricFilter object.
    """

    def __init__(self,
                 scope: Scope,
                 metricName: str,
                 operator: SegmentMetricFilterOperator =SegmentMetricFilterOperator.UNSPECIFIED_OPERATOR,
                 comparisonValue: str =None
                 maxComparisonValue: str =None
    ) -> None:
        """Initialises a SegmentMetricFilter object.
        """
        self['scope'] = scope
        self['metricName'] = metricName
        self['operator'] = operator
        self['comparisonValue'] = comparisonValue
        self['maxComparisonValue'] = maxComparisonValue


class SegmentFilterClause (dict):
    """A SegmentFilterClause object.
    """
    
    def __init__(self,
                 Not: bool =False,
                 dimensionOrMetricFilter: Union[SegmentDimensionFilter, SegmentMetricFilter] =None
    ) -> None
        """Initialises a SegmentFilterClause object.
        """
        self['not'] = Not

        # Based on the type of `dimensionOrMetricFilter`, assign it to either of
        # the two following keys.
        if isinstance(dimensionOrMetricFilter, SegmentDimensionFilter):
            self['dimensionFilter'] = dimensionOrMetricFilter
        elif isinstance(dimensionOrMetricFilter, SegmentMetricFilter):
            self['metricFilter'] = dimensionOrMetricFilter

class OrFiltersForSegment (dict):
    """An OrFiltersForSegment object.
    """

    def __init__(self,
                 segmentFilterClauses: list[SegmentFilterClause]
    ) -> None:
        """Initialises an OrFiltersForSegment object.
        """
        self['segmentFilterClauses'] = segmentFilterClauses

class SimpleSegment (dict):
    """A SimpleSegment object.
    """

    def __init__(self,
                 orFiltersForSegment: list[OrFiltersForSegment]
    ) -> None:
        """Initialises a SimpleSegment object.
        """
        self['orFiltersForSegment'] = orFiltersForSegment

class MatchType (Enum):
    """A MatchType object.
    """

    PRECEDES = "PRECEDES",
    IMMEDIATELY_PRECEDES = "IMMEDIATELY_PRECEDES"
    UNSPECIFIED_MATCH_TYPE = "PRECEDES"

class SegmentSequenceStep (dict):
    """A SegmentSequenceStep object.
    """

    def __init__(self,
                 orFiltersForSegment: list[OrFiltersForSegment],
                 matchType: MatchType =MatchType.UNSPECIFIED_MATCH_TYPE
    ) -> None:
        """Initialises a SegmentSequenceStep object.
        """
        self['orFiltersForSegment'] = orFiltersForSegment
        self['matchType'] = matchType

class SequenceSegment (dict):
    """A SequenceSegment object.
    """

    def __init__(self,
                 segmentSequenceSteps: list[SegmentSequenceStep],
                 firstStepShouldMatchFirstHit: bool =False
    ) -> None:
        """Initialises a SequenceSegment object.
        """
        self['segmentSequenceSteps'] = segmentSequenceSteps
        self['firstStepShouldMatchFirstHit'] = firstStepShouldMatchFirstHit

class SegmentFilter (dict):
    """A SegmentFilter object.
    """

    def __init__(self,
                 Not: bool =False,
                 simpleOrSequence: Union[SimpleSegment, SequenceSegment] =None
    ) -> None:
        """Initialises a SegmentFilter object.
        """
        self['not'] = Not

        # Based on the type of `simpleOrSequence`, assign it to either of
        # the two following keys.
        if isinstance(simpleOrSequence, SimpleSegment):
            self['simpleSegment'] = simpleOrSequence
        elif isinstance(simpleOrSequence, SequenceSegment):
            self['sequenceSegment'] = simpleOrSequence

class SegmentDefinition (dict):
    """A SegmentDefinition object.
    """

    def __init__(self,
                 segmentFilters: list[SegmentFilter]
    ) -> None:
        """Initialises a SegmentDefinition object.
        """
        self['segmentFilters'] = segmentFilters

class DynamicSegment (dict):
    """A DynamicSegment object.
    """

    def __init__(self,
                 name: str,
                 userSegment: SegmentDefinition,
                 sessionSegment: SegmentDefinition
    ) -> None:
        """Initialises a DynamicSegment object.
        """
        self['name'] = name
        self['userSegment'] = userSegment
        self['sessionSegment'] = sessionSegment

class Segment (dict):
    """A Segment object.
    """

    def __init__(self,
                 dynamicOrById: Union[DynamicSegment, str]
    ) -> None:
        """Initialises a Segment object.
        """
        # Based on the type of `dynamicOrById`, assign it to either of the two
        # following keys.
        if isinstance(dynamicOrById, DynamicSegment):
            self['dynamicSegment'] = dynamicOrById
        elif isinstance(dynamicOrById, str):
            self['segmentId'] = dynamicOrById
