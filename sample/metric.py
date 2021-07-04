from enum import Enum

class MetricType (Enum):
    METRIC_TYPE_UNSPECIFIED = "METRIC_TYPE_UNSPECIFIED",
    INTEGER = "INTEGER",
    FLOAT = "FLOAT",
    CURRENCY = "CURRENCY",
    PERCENT = "PERCENT",
    TIME = "TIME"

class Metric (dict):

    def __init__(self,
                 expression: str= '',
                 alias: str ='',
                 formattingType=MetricType.METRIC_TYPE_UNSPECIFIED):
        self['expression'] = expression
        self['alias'] = alias
        self['formattingType'] = formattingType

class Operator (Enum):
    OPERATOR_UNSPECIFIED = "OPERATOR_UNSPECIFIED",
    EQUAL = "EQUAL",
    LESS_THAN = "LESS_THAN",
    GREATER_THAN = "GREATER_THAN",
    IS_MISSING = "IS_MISSING"

class MetricFilter (dict):

    def __init__(self,
                 metricName: str ='',
                 Not: bool =false,
                 operator: Operator.EQUAL,
                 comparisonValue: str =''):
        self['metricName'] = metricName
        self['not'] = Not
        self['operator'] = operator
        self['comparisonValue'] = comparisonValue
