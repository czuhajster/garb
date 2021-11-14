from garb import report_request

def test_report_request():
    """
    Tests `ReportRequest` class.
    """

    pass

def test_request_body_to_json():
    """
    Tests `RequestBody` class conversion to JSON string.
    """

    reportBody =  report_request.RequestBody([])
    reportBodyJson = reportBody.json()
    assert reportBodyJson == '{"reportRequests": [], "useResourceQuotas": false}'
