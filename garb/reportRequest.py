from enum import Enum

from .daterange import DateRange
from .order import *
from .metric import *
from .dimension import *
from .pivot import *
from .cohort import *


class Sampling(Enum):
    DEFAULT = 'DEFAULT',
    SMALL = 'SMALL',
    LARGE = 'LARGE',
    SAMPLING_UNSPECIFIED = 'DEFAULT'

class ReportRequest (dict):

    def __init__(self,
                 viewID: str,
                 dateRanges: list[DateRange] =[],
                 samplingLevel: Sampling =Sampling.SAMPLING_UNSPECIFIED,
                 dimensions: list[Dimension] =[],
                 dimensionFilterClauses: list[DimensionFilterClause] =[],
                 metrics: list[Metric] =[],
                 metricFilterClauses: list[MetricFilterClause]= [],
                 filtersExpression: str ='',
                 orderBys: list[OrderBy] =[],
                 segments: list =[],
                 pivots: list[Pivot] =[],
                 cohortGroup: CohortGroup =None,
                 pageToken: str =None,
                 pageSize: int =None,
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

class RequestBody (dict):

    def __init__(self,
                 reportRequests: list[ReportRequest] =[],
                 useResourceQuotas: bool =False):
        self['reportRequests'] = reportRequests
        self['useResourceQuotas'] = useResourceQuotas

    def addReportRequest(self, reportRequest: ReportRequest =None):
        if reportRequest is not None:
            self['reportRequests'].append(reportRequest)
