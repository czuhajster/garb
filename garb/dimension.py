"""Dimension module

This module defines dimenion-related objects: Dimension, DimensionOperator, and
DimensionFilterClause.
"""

from enum import *

from .filter_logical_operator import FilterLogicalOperator

class Dimension (dict):
    """A dimension object.
    """

    def __init__(self,
                 name: str =None,
                 histrogramBuckets: list[str] =None
    ) -> None:
        """Initialises a dimension object.
        """
        self['name'] = name
        self['histrogramBuckets'] = histrogramBuckets

class DimensionOperator(str, Enum):
    """A dimension operator object.

    Dimension operator object is used in DimensionFilter object to specify how a
    dimension is filtered.
    """

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
    """A dimension filter object.

    Dimension filter specifies how a dimension should be filtered.
    """

    def __init__(self,
                 dimensionName: str,
                 Not: bool =False,
                 operator: DimensionOperator =DimensionOperator.OPERATOR_UNSPECIFIED,
                 expressions: list[str] =None,
                 caseSensitive: bool =False
    ) -> None:
        """Initialises a dimension filter object.
        """
        self['dimensionName'] = dimensionName
        self['not'] = Not
        self['operator'] = operator
        self['expressions'] = expressions
        self['caseSensitive'] = caseSensitive

class DimensionFilterClause(dict):
    """A dimension filter clause object.
    """

    def __init__(self,
                 operator: FilterLogicalOperator =FilterLogicalOperator.OPERATOR_UNSPECIFIED,
                 filters: list[DimensionFilter] =None
    ) -> None:
        """Initialises a dimension filter clause object.
        """
        self['operator'] = operator
        self['filters'] = filters
