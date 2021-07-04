from enum import Enum

class OrderType (Enum):
    ORDER_TYPE_UNSPECIFIED = "ORDER_TYPE_UNSPECIFIED",
    VALUE = "VALUE",
    DELTA = "DELTA",
    SMART = "SMART",
    HISTOGRAM_BUCKET = "HISTOGRAM_BUCKET",
    DIMENSION_AS_INTEGER = "DIMENSION_AS_INTEGER"

class SortOrder (Enum):
    SORT_ORDER_UNSPECIFIED = "SORT_ORDER_UNSPECIFIED",
    ASCENDING = "ASCENDING",
    DESCENDING = "DESCENDING"

class OrderBy (dict):

    def __init__(self,
                 fieldName: str,
                 orderType: OrderType =OrderType.VALUE,
                 sortOrder: SortOrder =SortOrder.ASCENDING):
