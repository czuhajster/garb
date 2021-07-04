from enum import *

class Dimension (dict):

    def __init__(self, name: str ='', histrogramBuckets: list =[]):
        self['name'] = name
        self['histrogramBuckets'] = histrogramBuckets


class Operator(str, Enum):
    OPERATOR_UNSPECIFIED = "OPERATOR_UNSPECIFIED",
    REGEXP = "REGEXP",
    BEGINS_WITH = "BEGINS_WITH",
    ENDS_WITH = "ENDS_WITH",
    PARTIAL = "PARTIAL",
    EXACT = "EXACT",
    NUMERIC_EQUAL = "NUMERIC_EQUAL",
    NUMERIC_GREATER_THAN = "NUMERIC_GREATER_THAN",
    NUMERIC_LESS_THAN = "NUMERIC_LESS_THAN",
    IN_LIST = "IN_LIST"

class FilterLogicalOperator (Enum):
    OPERATOR_UNSPECIFIED = "OPERATOR_UNSPECIFIED",
    OR = "OR",
    AND = "AND"

class DimensionFilter(dict):

    def __init__(self,
                 dimensionName: str,
                 Not: bool =False,
                 operator: Operator =Operator.REGEXP,
                 expressions: list =[],
                 caseSensitive: bool =False):
        self['dimensionName'] = dimensionName
        self['not'] = Not
        self['operator'] = operator
        self['expressions'] = expressions
        self['caseSensitive'] = caseSensitive

class DimensionFilterClause(dict):

    def __init__(self,
                 operator: FilterLogicalOperator ='OR',
                 filters: list =[]):
        self['operator'] = operator
        self['filters'] = filters

    def addDimensionFilter(self, dimensionName: str, Not: bool =False,
                           operator: str ='', expressions: list =[],
                           caseSensitive: bool =False):
        newDimensionFilter = DimensionFilter(dimensionName, Not, operator,
                                             expressions, caseSensitive)
        self['filters'].append(newDimensionFilter)


