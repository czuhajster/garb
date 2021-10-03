from garb import *

def test_metric():
    """
    Test Metric class.
    """

    pass

def test_metric_filter_clause():
    """
    Test MetricFilterClause class.
    """

    pass

def test_metric_filter():
    """
    Test MetricFilter class.
    """

    metricFilter = metric.MetricFilter("sessions", False, "EQUAL", "220")

    assert metricFilter['metricName'] == "sessions"
    assert metricFilter['not'] == False
    assert metricFilter['operator'] == "EQUAL"
    assert metricFilter['comparisonValue'] == "220"

def test_metric_filter_clause():
    """
    Test MetricFilterClause class.
    """

    metricFilter = metric.MetricFilter("sessions", False, "EQUAL", "220")
    metricFilterClause = metric.MetricFilterClause("OR", [metricFilter])

    assert metricFilterClause['operator'] == "OR"
    assert metricFilterClause['filters'][0] is metricFilter


