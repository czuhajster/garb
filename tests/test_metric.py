from garb import *

def test_metric():
    """
    Test Metric class.
    """

    a_metric = metric.Metric("ga:sessions", "sessions")
    assert a_metric == {
        "expression": "ga:sessions",
        "alias": "sessions",
        "formattingType": metric.MetricType.INTEGER
    }

    pass

def test_metric_filter():
    """
    Test MetricFilter class.
    """

    metricFilter = metric.MetricFilter("sessions", "220", False, "EQUAL")

    assert metricFilter['metricName'] == "sessions"
    assert metricFilter['comparisonValue'] == "220"
    assert metricFilter['not'] == False
    assert metricFilter['operator'] == "EQUAL"

def test_metric_filter_clause():
    """
    Test MetricFilterClause class.
    """

    metricFilter = metric.MetricFilter("sessions", "220", False, "EQUAL")
    metricFilterClause = metric.MetricFilterClause([metricFilter], "OR")

    assert metricFilterClause['filters'][0] is metricFilter
