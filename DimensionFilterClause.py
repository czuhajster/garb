from enum import *
from Operator import Operator

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


