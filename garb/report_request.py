"""ReportRequest module

This module defines Sampling, ReportRequest, and RequestBody objects.
"""

from enum import Enum
import json

from garb.daterange import DateRange
from garb.metric import Metric, MetricFilterClause
from garb.dimension import Dimension, DimensionFilterClause
from garb.order import OrderBy
from garb.pivot import Pivot
from garb.cohort import CohortGroup

class Sampling(Enum):
    """A Sampling object.
    """

    DEFAULT = 'DEFAULT'
    SMALL = 'SMALL'
    LARGE = 'LARGE'
    SAMPLING_UNSPECIFIED = 'DEFAULT'

class ReportRequest (dict):
    """A ReportRequest object.
    """

    def __init__(self,
                 view_id: str,
                 dateranges: list[DateRange],
                 metrics: list[Metric],
                 metric_filter_clauses: list[MetricFilterClause] =None,
                 sampling_level: Sampling =Sampling.SAMPLING_UNSPECIFIED,
                 dimensions: list[Dimension] =None,
                 dimension_filter_clauses: list[DimensionFilterClause] =None,
                 filters_expression: str =None,
                 order_bys: list[OrderBy] =None,
                 segments: list =None,
                 pivots: list[Pivot] =None,
                 cohort_group: CohortGroup =None,
                 page_token: str =None,
                 page_size: int =None,
                 include_empty_rows: bool =False,
                 hide_totals: bool =False,
                 hide_value_ranges: bool =False
    ) -> None:
        """Initialises a report request object.

        Args:
          view_id
          dateranges
          metrics
          metric_filter_clauses
          sampling_level
          dimensions
          dimension_filter_clauses
          filters_expression
          order_bys
          segments
          pivots
          cohort_group
          page_token
          page_size
          include_empty_rows
          hide_totals
          hide_value_ranges

        Returns:
          None
        """
        self['viewID'] = view_id
        self['dateRanges'] = dateranges
        self['metrics'] = metrics
        if metric_filter_clauses is not None:
            self['metricFilterClauses'] = metric_filter_clauses
        if sampling_level != Sampling.SAMPLING_UNSPECIFIED:
            self['samplingLevel'] = sampling_level
        if dimensions is not None:
            self['dimensions'] = dimensions
        if dimension_filter_clauses is not None:
            self['dimensionFilterClauses'] = dimension_filter_clauses
        if filters_expression is None:
            self['filtersExpression'] = filters_expression
        if order_bys is not None:
            self['orderBys'] = order_bys
        if segments is not None:
            self['segments'] = segments
        if pivots is not None:
            self['pivots'] = pivots
        if cohort_group is not None:
            self['cohortGroup'] = cohort_group
        if page_token is not None:
            self['pageToken'] = page_token
        self['pageSize'] = page_size
        if not include_empty_rows:
            self['includeEmptyRows'] = include_empty_rows
        if not hide_totals:
            self['hideTotals'] = hide_totals
        if not hide_value_ranges:
            self['hideValueRanges'] = hide_value_ranges

class RequestBody (dict):
    """
    A request body object.
    """

    def __init__(self,
                 report_requests: list[ReportRequest],
                 use_resource_quotas: bool =False
    ) -> None:
        """Initialises a request body object.

        Args:
          report_requests:
          use_resource_quotas:

        Returns:
          None
        """
        self['reportRequests'] = report_requests
        if not use_resource_quotas:
            self['useResourceQuotas'] = use_resource_quotas

    def add_report_request(self, report_request: ReportRequest =None):
        """Appends a report request object to the list of reportRequests.

        Args:
          report_request:

        Returns:
          None
        """
        self['reportRequests'].append(report_request)

    def json(self):
        """Converts request body object to JSON representation.

        Returns:
          A JSON representation of the request body object.
        """
        return json.dumps(self)
