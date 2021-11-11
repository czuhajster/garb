from garb import daterange

def test_daterange():
    """
    Tests `DateRange` class.
    """
    a_daterange = daterange.DateRange("2021-01-01", "2021-01-31")
    assert a_daterange == {
        "startDate": "2021-01-01",
        "endDate": "2021-01-31"
    }
