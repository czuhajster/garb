"""Pivot module

This module defines the pivot object.
"""

from .dimension import Dimension, DimensionFilterClause
from .metric import Metric

class Pivot (dict):
    """A pivot object.
    """

    def __init__(self,
                 dimensions: list[Dimension],
                 dimensionFilterClauses: list[DimensionFilterClause],
                 metrics: list[Metric],
                 startGroup: int,
                 maxGroupCount: int =10
    ) -> None:
        """Initialises a pivot object.
        """
        self['dimensions'] = dimensions
        self['dimensionFilterClauses'] = dimensionFilterClauses
        self['metrics'] = metrics
        self['startGroup'] = startGroup
        self['maxGroupCount'] = maxGroupCount
