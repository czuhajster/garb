"""Metric module

This module defines metric-related objects: MetricType, Metric, MetricOperator,
MetricFilter, MetricFilterClause.
"""

from enum import Enum

from .filter_logical_operator import FilterLogicalOperator


class MetricType (Enum):
    INTEGER = "INTEGER",
    FLOAT = "FLOAT",
    CURRENCY = "CURRENCY",
    PERCENT = "PERCENT",
    TIME = "TIME",
    METRIC_TYPE_UNSPECIFIED = "INTEGER",


class Metric (dict):
    """A metric object.
    """

    def __init__(self,
                 expression: str= None,
                 alias: str = None
                 formattingType: MetricType =MetricType.METRIC_TYPE_UNSPECIFIED
    ) -> None:
        """
        Initialises a Metric object.
        """
        self['expression'] = expression
        if alias is not None:
            self['alias'] = alias
        self['formattingType'] = formattingType

    def setAlias(self, alias: str) -> None:
        self['alias'] = alias

    def setExpression(self, expression: str) -> None:
        self['expression'] = expression

    def setFormattingType(self, formattingType: MetricType) -> None:
        self['formattingType'] = formattingType


class MetricOperator (Enum):
    EQUAL = "EQUAL",
    LESS_THAN = "LESS_THAN",
    GREATER_THAN = "GREATER_THAN",
    IS_MISSING = "IS_MISSING",
    OPERATOR_UNSPECIFIED = "EQUAL",


class MetricFilter (dict):
    """A metric filter object.
    """

    def __init__(self,
                 metricName: str,
                 Not: bool =False,
                 operator: MetricOperator =MetricOperator.EQUAL,
                 comparisonValue: str =None
    ) -> None:
        """Initialises a metric filter object.
        """
        self['metricName'] = metricName
        self['not'] = Not
        self['operator'] = operator
        self['comparisonValue'] = comparisonValue


class MetricFilterClause (dict):
    """A metric filter object.
    """

    def __init__(self,
                 operator: FilterLogicalOperator =FilterLogicalOperator.OPERATOR_UNSPECIFIED,
                 filters: list[MetricFilter]= None) -> None:
        """
        Initialises a MetricFilterClause object.
        """
        self['operator'] = operator
        if filters is not None:
            self['filters'] = filters
