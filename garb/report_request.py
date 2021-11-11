"""ReportRequest module

This module defines Sampling, ReportRequest, and RequestBody objects.
"""

from enum import Enum
import json

from .daterange import DateRange
from .order import *
from .metric import *
from .dimension import *
from .pivot import *
from .cohort import *


class Sampling(Enum):
    """A Sampling object.
    """

    DEFAULT = 'DEFAULT',
    SMALL = 'SMALL',
    LARGE = 'LARGE',
    SAMPLING_UNSPECIFIED = 'DEFAULT'

class ReportRequest (dict):
    """A ReportRequest object.
    """

    def __init__(self,
                 viewID: str,
                 dateRanges: list[DateRange],
                 metrics: list[Metric],
                 metricFilterClauses: list[MetricFilterClause] =None,
                 samplingLevel: Sampling =Sampling.SAMPLING_UNSPECIFIED,
                 dimensions: list[Dimension] =None,
                 dimensionFilterClauses: list[DimensionFilterClause] =None,
                 filtersExpression: str =None,
                 orderBys: list[OrderBy] =None,
                 segments: list =None,
                 pivots: list[Pivot] =None,
                 cohortGroup: CohortGroup =None,
                 pageToken: str =None,
                 pageSize: int =None,
                 includeEmptyRows: bool =False,
                 hideTotals: bool =False,
                 hideValueRanges: bool =False
    ) -> None:
        """Initialises a report request object.

        Args:
          dateRanges
          metrics
          metricFilterClauses
          samplingLevel
          dimensions
          dimensionFilterClauses
          filtersExpression
          orderBys
          segments
          pivots
          cohortGroup
          pageToken
          pageSize
          includeEmptyRows
          hideTotals
          hideValueRanges

        Returns:
          None
        """
        self['viewID'] = viewID
        self['dateRanges'] = dateRanges
        self['metrics'] = metrics
        if metricFilterClauses is not None:
            self['metricFilterClauses'] = metricFilterClauses
        if samplingLevel != Sampling.SAMPLING_UNSPECIFIED:
            self['samplingLevel'] = samplingLevel
        if dimensions is not None:
            self['dimensions'] = dimensions
        if dimensionFilterClauses is not None:
            self['dimensionFilterClauses'] = dimensionFilterClauses
        if filtersExpression is None:
            self['filtersExpression'] = filtersExpression
        if orderBys is not None:
            self['orderBys'] = orderBys
        if segments is not None:
            self['segments'] = segments
        if pivots is not None:
            self['pivots'] = pivots
        if cohortGroup is not None:
            self['cohortGroup'] = cohortGroup
        if pageToken is not None:
            self['pageToken'] = pageToken
        self['pageSize'] = pageSize
        if not includeEmptyRows:
            self['includeEmptyRows'] = includeEmptyRows
        if not hideTotals:
            self['hideTotals'] = hideTotals
        if not hideValueRanges:
            self['hideValueRanges'] = hideValueRanges

class RequestBody (dict):
    """
    A request body object.
    """

    def __init__(self,
                 reportRequests: list[ReportRequest],
                 useResourceQuotas: bool =False
    ) -> None:
        """Initialises a request body object.

        Args:
          reportRequests:
          useResourceQuotas:

        Returns:
          None
        """
        self['reportRequests'] = reportRequests
        if not useResourceQuotas:
            self['useResourceQuotas'] = useResourceQuotas

    def addReportRequest(self, reportRequest: ReportRequest =None):
        """Appends a report request object to the list of reportRequests.

        Args:
          self:
          reportRequest:

        Returns:
          None
        """
        self['reportRequests'].append(reportRequest)

    def json(self):
        """Converts request body object to JSON representation.

        Returns:
          A JSON representation of the request body object.
        """
        return json.dumps(self)
