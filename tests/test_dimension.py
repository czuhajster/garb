from garb import *

def test_dimension():
    """
    Tests `Dimension` class.
    """
    a_dimension = dimension.Dimension("ga:dimension")

    assert a_dimension == {
        "name": "ga:dimension",
        "histrogramBuckets": None
    }

def test_dimension_filter():
    """
    Tests `DimensionFilter` class.
    """

    dimension_filter = dimension.DimensionFilter("ga:dimension", False,
                                                 "REGEXP", None, False)

    assert dimension_filter == {
        "dimensionName": "ga:dimension",
        "not": False,
        "operator": "REGEXP",
        "expressions": None,
        "caseSensitive": False
    }
