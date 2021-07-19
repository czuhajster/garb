from enum import *
from FilterLogicalOperator import FilterLogicalOperator

class Dimension (dict):

    def __init__(self, name: str ='', histrogramBuckets: list[str] =[]) -> None:
        self['name'] = name
        self['histrogramBuckets'] = histrogramBuckets

class DimensionOperator(str, Enum):
    REGEXP = "REGEXP",
    BEGINS_WITH = "BEGINS_WITH",
    ENDS_WITH = "ENDS_WITH",
    PARTIAL = "PARTIAL",
    EXACT = "EXACT",
    NUMERIC_EQUAL = "NUMERIC_EQUAL",
    NUMERIC_GREATER_THAN = "NUMERIC_GREATER_THAN",
    NUMERIC_LESS_THAN = "NUMERIC_LESS_THAN",
    IN_LIST = "IN_LIST",
    OPERATOR_UNSPECIFIED = "REGEXP",

class DimensionFilter(dict):

    def __init__(self,
                 dimensionName: str,
                 Not: bool =False,
                 operator: DimensionOperator =DimensionOperator.OPERATOR_UNSPECIFIED,
                 expressions: list[str] =[],
                 caseSensitive: bool =False):
        self['dimensionName'] = dimensionName
        self['not'] = Not
        self['operator'] = operator
        self['expressions'] = expressions
        self['caseSensitive'] = caseSensitive

class DimensionFilterClause(dict):

    def __init__(self,
                 operator: FilterLogicalOperator =FilterLogicalOperator.OPERATOR_UNSPECIFIED,
                 filters: list[DimensionFilter] =[]):
        self['operator'] = operator
        self['filters'] = filters
