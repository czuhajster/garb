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

# ...


date_ranges = [garb.daterange.DateRange('7daysAgo', 'today')]
metrics = [garb.metric.Metric('ga:sessions')]
report_requests = [garb.report_request.ReportRequest(VIEW_ID, date_ranges, metrics)]
request_body = garb.report_request.RequestBody(report_requests)
```

2. Pass a `RequestBody` object as a parameter to the `batchGet` method:

```python
def get_report(analytics):
    return analytics.reports().batchGet(body=request_body).execute()
```

## License

GARB is licensed under [MIT License](https://github.com/czuhajster/garb/blob/main/LICENSE.md).
