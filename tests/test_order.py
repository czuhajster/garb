from garb import order

def test_order_by():
    """
    Tests `OrderBy` class.
    """
    order_by = order.OrderBy("ga:browser", order.OrderType.VALUE, order.SortOrder.ASCENDING)
    assert order_by == {
        "fieldName": "ga:browser",
        "orderType": order.OrderType.VALUE,
        "sortOrder": order.SortOrder.ASCENDING
    }
