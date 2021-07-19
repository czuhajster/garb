from enum import Enum
from typing import Union

class SegmentDimensionFilterOperator(Enum):
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

    def __init__(self,
                 dimensionName: str,
                 operator: SegmentDimensionFilterOperator =SegmentDimensionFilterOperator.OPERATOR_UNSPECIFIED,
                 caseSensitive: bool =False,
                 expressions: list[str] =[],
                 minComparisonValue: str ='',
                 maxComparisonValue: str =''):
        self['dimensionName'] = dimensionName
        self['operator'] = operator
        self['caseSensitive'] = caseSensitive
        self['expressions'] = expressions
        self['minComparisonValue'] = minComparisonValue
        self['maxComparisonValue'] = maxComparisonValue

class SegmentMetricFilterOperator (Enum):
    LESS_THAN = "LESS_THAN",
    GREATER_THAN = "GREATER_THAN",
    EQUAL = "EQUAL",
    BETWEEN = "BETWEEN"
    UNSPECIFIED_OPERATOR = "LESS_THAN"

class Scope (Enum):
    PRODUCT = "PRODUCT",
    HIT = "HIT",
    SESSION = "SESSION",
    USER = "USER"
    # TODO: implement `UNSPECIFIED_SCOPE` to default either to `USER` or
    # `SESSION`.

class SegmentMetricFilter (dict):

    def __init__(self,
                 scope: Scope,
                 metricName: str,
                 operator: SegmentMetricFilterOperator =SegmentMetricFilterOperator.UNSPECIFIED_OPERATOR,
                 comparisonValue: str ='',
                 maxComparisonValue: str =''):
        self['scope'] = scope
        self['metricName'] = metricName
        self['operator'] = operator
        self['comparisonValue'] = comparisonValue
        self['maxComparisonValue'] = maxComparisonValue


class SegmentFilterClause (dict):
    
    def __init__(self,
                 Not: bool =False,
                 dimensionOrMetricFilter: Union[SegmentDimensionFilter,
                                                SegmentMetricFilter] =None):
        self['not'] = Not

        # Based on the type of `dimensionOrMetricFilter`, assign it to either of
        # the two following keys.
        if isinstance(dimensionOrMetricFilter, SegmentDimensionFilter):
            self['dimensionFilter'] = dimensionOrMetricFilter
        elif isinstance(dimensionOrMetricFilter, SegmentMetricFilter):
            self['metricFilter'] = dimensionOrMetricFilter

class OrFiltersForSegment (dict):

    def __init__(self,
                 segmentFilterClauses: list[SegmentFilterClause]):
        self['segmentFilterClauses'] = segmentFilterClauses

class SimpleSegment (dict):
    def __init__(self,
                 orFiltersForSegment: list[OrFiltersForSegment]):
        self['orFiltersForSegment'] = orFiltersForSegment

class MatchType (Enum):
    PRECEDES = "PRECEDES",
    IMMEDIATELY_PRECEDES = "IMMEDIATELY_PRECEDES"
    UNSPECIFIED_MATCH_TYPE = "PRECEDES"

class SegmentSequenceStep (dict):

    def __init__(self,
                 orFiltersForSegment: list[OrFiltersForSegment],
                 matchType: MatchType =MatchType.UNSPECIFIED_MATCH_TYPE):
        self['orFiltersForSegment'] = orFiltersForSegment
        self['matchType'] = matchType

class SequenceSegment (dict):

    def __init__(self,
                 segmentSequenceSteps: list[SegmentSequenceStep],
                 firstStepShouldMatchFirstHit: bool =False):
        self['segmentSequenceSteps'] = segmentSequenceSteps
        self['firstStepShouldMatchFirstHit'] = firstStepShouldMatchFirstHit

class SegmentFilter (dict):
    def __init__(self,
                 Not: bool =False,
                 simpleOrSequence: Union[SimpleSegment, SequenceSegment] =None):
        self['not'] = Not

        # Based on the type of `simpleOrSequence`, assign it to either of
        # the two following keys.
        if isinstance(simpleOrSequence, SimpleSegment):
            self['simpleSegment'] = simpleOrSequence
        elif isinstance(simpleOrSequence, SequenceSegment):
            self['sequenceSegment'] = simpleOrSequence

class SegmentDefinition (dict):
    def __init__(self,
                 segmentFilters: list[SegmentFilter]):
        self['segmentFilters'] = segmentFilters

class DynamicSegment (dict):

    def __init__(self,
                 name: str,
                 userSegment: SegmentDefinition,
                 sessionSegment: SegmentDefinition):
        self['name'] = name
        self['userSegment'] = userSegment
        self['sessionSegment'] = sessionSegment

class Segment (dict):

    def __init__(self,
                 dynamicOrById: Union[DynamicSegment, str]):
        # Based on the type of `dynamicOrById`, assign it to either of the two
        # following keys.
        if isinstance(dynamicOrById, DynamicSegment):
            self['dynamicSegment'] = dynamicOrById
        elif isinstance(dynamicOrById, str):
            self['segmentId'] = dynamicOrById
