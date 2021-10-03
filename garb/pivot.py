from .dimension import Dimension, DimensionFilterClause
from .metric import Metric

class Pivot (dict):

    def __init__(self,
                 dimensions: list[Dimension],
                 dimensionFilterClauses: list[DimensionFilterClause],
                 metrics: list[Metric],
                 startGroup: int,
                 maxGroupCount: int =10):
        self['dimensions'] = dimensions
        self['dimensionFilterClauses'] = dimensionFilterClauses
        self['metrics'] = metrics
        self['startGroup'] = startGroup
        self['maxGroupCount'] = maxGroupCount
