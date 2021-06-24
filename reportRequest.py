from enum import *


class ReportRequest (dict):

    def __init__(self,
                 viewID: str,
                 dateRanges: list =[],
                 samplingLevel: SamplingLevel =None,
                 dimensions: list =[],
                 dimensionFilterClauses: list =[],
                 metrics: list =[],
                 metricFilterClauses: list = [],
                 filtersExpression: str ='',
                 orderBys: list =[],
                 segments: list =[],
                 pivots: list =[],
                 cohortGroup: str = '',
                 pageToken: str =None,
                 pageSize: str =None,
                 includeEmptyRows: bool =False,
                 hideTotals: bool =False,
                 hideValueRanges: bool =False):
        self['viewID'] = viewID
        self['dateRanges'] = dateRanges
        self['samplingLevel'] = samplingLevel
        self['dimensions'] = dimensions
        self['dimensionFilterClauses'] = dimensionFilterClauses
        self['metrics'] = metrics
        self['metricFilterClauses'] = metricFilterClauses
        self['filtersExpression'] = filtersExpression
        self['orderBys'] = orderBys
        self['segments'] = segments
        self['pivots'] = pivots
        self['cohortGroup'] = cohortGroup
        self['pageToken'] = pageToken
        self['pageSize'] = pageSize
        self['includeEmptyRows'] = includeEmptyRows
        self['hideTotals'] = hideTotals
        self['hideValueRanges'] = hideValueRanges

class DateRange(dict):

    def __init__(self, startDate: str, endDate: str):
        """Initialise attributes in format 'YYYY-MM-DD'"""
        self['startDate'] = startDate
        self['endDate'] = endDate

@unique
class SamplingLevel(str, Enum):
    SAMPLING_UNSPECIFIED = 'SAMPLING_UNSPECIFIED',
    DEFAULT = 'DEFAULT',
    SMALL = 'SMALL',
    LARGE = 'LARGE'

class Dimension(dict):

    def __init__(self, name: str, histogramBuckets: list =[]):
        self['name'] = name
        self['histogramBuckets'] = histogramBuckets


class Metric(dict):

    def __init__(self, expression: str, alias: str ='', formattingType: str =''):
        self['expression'] = expression
        self['alias'] = alias
        self['formattingType'] = formattingType

class RequestBody (dict):

    def __init__(self,
                 reportRequests: list =[],
                 useResourceQuotas: bool =False):
        self['reportRequests'] = reportRequests
        self['useResourceQuotas'] = useResourceQuotas

    def addReportRequest(self, reportRequest: ReportRequest =None):
        if reportRequest is not None:
            self['reportRequests'].append(reportRequest)

# Add abstract class

newDateRange = DateRange('2021-01-01', '2021-01-31')
dimension = Dimension('ga:day')
dimensionFilterClauses = DimensionFilterClauses()
dimensionFilterClauses.addDimensionFilter('ga:eventLabel', False, 'EXACT',
                                          ['Service form'])
metric = Metric('ga:totalEvent', formattingType='INTEGER')
newReportRequest = ReportRequest('161838420', [newDateRange], [dimension],
                                 dimensionFilterClauses, [metric])

print(newReportRequest)
