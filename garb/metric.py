from enum import Enum
from FilterLogicalOperator import FilterLogicalOperator

class MetricType (Enum):
    INTEGER = "INTEGER",
    FLOAT = "FLOAT",
    CURRENCY = "CURRENCY",
    PERCENT = "PERCENT",
    TIME = "TIME",
    METRIC_TYPE_UNSPECIFIED = "INTEGER",

class Metric (dict):

    def __init__(self,
                 expression: str= '',
                 alias: str ='',
                 formattingType: MetricType =MetricType.METRIC_TYPE_UNSPECIFIED) -> None:
        self['expression'] = expression
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

    def __init__(self,
                 metricName: str ='',
                 Not: bool =False,
                 operator: MetricOperator =MetricOperator.OPERATOR_UNSPECIFIED,
                 comparisonValue: str =''):
        self['metricName'] = metricName
        self['not'] = Not
        self['operator'] = operator
        self['comparisonValue'] = comparisonValue

class MetricFilterClause (dict):

    def __init__(self,
                 operator: FilterLogicalOperator =FilterLogicalOperator.OPERATOR_UNSPECIFIED,
                 filters: list[MetricFilter]= []) -> None:
        self['operator'] = operator
        self['filters'] = filters

if __name__ == "__main__":
    metric = Metric(40, '', False)
