# GARB - Google Analytics Request Builder
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Code Size](https://img.shields.io/github/languages/code-size/czuhajster/garb)
![Last Commit](https://img.shields.io/github/last-commit/czuhajster/garb)
![PyPI Version](https://img.shields.io/pypi/v/garb)

GARB is a small Python library that provides an object-oriented interface for building requests
for Google Analytics Reporting API v4.

## Installation

### Using pip

Install `garb` using [pip](https://pip.pypa.io/en/stable/quickstart/):

    pip install garb

## Usage

### Using Google API Client

1. Build a request body, e.g.:

```python
import garb

...


dateRanges = [garb.daterange.DateRange('7daysAgo', 'today')]
metrics = [garb.daterange.Metric('ga:sessions')]
reportRequests = [garb.report_request.ReportRequest(VIEW_ID, dateRanges, metrics)]
reportBody = garb.report_request.ReportBody(reportRequests)
```

2. Pass the `ReportBody` as a parameter to the `batchGet` method:

```python
def get_report(analytics):
    return analytics.reports().batchGet(body=reportBody).execute()
```

## License

GARB is licensed under [MIT License](https://github.com/czuhajster/garb/blob/main/LICENSE.md).
