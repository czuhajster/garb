from garb import *

def test_conversion_to_dictionary():
    """
    Test conversion of `ReportRequest` object into dictionary.
    """

    pass

def test_json():
    """
    Test conversion to JSON string.
    """

    reportBody =  report_request.RequestBody()
    reportBodyJson = reportBody.json()
    print(reportBodyJson)
    assert reportBodyJson == '{"reportRequests": [], "useResourceQuotas": false}'

