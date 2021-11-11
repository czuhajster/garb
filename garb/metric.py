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
                 alias: str = None,
                 formattingType: MetricType =MetricType.METRIC_TYPE_UNSPECIFIED
    ) -> None:
        """
        Initialises a Metric object.
        """
        self['expression'] = expression
        if alias is not None:
            self['alias'] = alias
        self['formattingType'] = formattingType

    def set_alias(self, alias: str) -> None:
        """
        Sets alias for metric.

        Args:
            alias: alias for the metric
        """
        self['alias'] = alias

    def set_expression(self, expression: str) -> None:
        """
        Sets expression for the metric.

        Args:
            expression: expression for metric
        """
        self['expression'] = expression

    def set_formatting_type(self, formatting_type: MetricType) -> None:
        """
        Sets formatting type for the metric.

        Args:
            formatting_type: formatting type for the metric
        """
        self['formattingType'] = formatting_type


class MetricOperator (Enum):
    OPERATOR_UNSPECIFIED = "EQUAL",
    EQUAL = "EQUAL",
    LESS_THAN = "LESS_THAN",
    GREATER_THAN = "GREATER_THAN",
    IS_MISSING = "IS_MISSING",


class MetricFilter (dict):
    """A metric filter object.
    """

    def __init__(self,
                 metricName: str,
                 comparisonValue: str,
                 Not: bool =False,
                 operator: MetricOperator =MetricOperator.OPERATOR_UNSPECIFIED
    ) -> None:
        """Initialises a metric filter object.
        """
        self['metricName'] = metricName
        self['comparisonValue'] = comparisonValue
        if not Not:
            self['not'] = Not
        if operator != MetricOperator.OPERATOR_UNSPECIFIED:
            self['operator'] = operator


class MetricFilterClause (dict):
    """A metric filter object.
    """

    def __init__(self,
                 filters: list[MetricFilter],
                 operator: FilterLogicalOperator =FilterLogicalOperator.OPERATOR_UNSPECIFIED,
    ) -> None:
        """
        Initialises a MetricFilterClause object.
        """
        self['filters'] = filters
        if operator != FilterLogicalOperator.OPERATOR_UNSPECIFIED:
            self['operator'] = operator
