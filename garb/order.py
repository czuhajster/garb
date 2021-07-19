from enum import Enum

class OrderType (Enum):
    VALUE = "VALUE",
    DELTA = "DELTA",
    SMART = "SMART",
    HISTOGRAM_BUCKET = "HISTOGRAM_BUCKET",
    DIMENSION_AS_INTEGER = "DIMENSION_AS_INTEGER",
    ORDER_TYPE_UNSPECIFIED = "VALUE"

class SortOrder (Enum):
    ASCENDING = "ASCENDING",
    DESCENDING = "DESCENDING",
    SORT_ORDER_UNSPECIFIED = "ASCENDING",

class OrderBy (dict):

    def __init__(self,
                 fieldName: str,
                 orderType: OrderType =OrderType.ORDER_TYPE_UNSPECIFIED,
                 sortOrder: SortOrder =SortOrder.SORT_ORDER_UNSPECIFIED):
        self['fieldName'] = fieldName
        self['orderType'] = orderType
        self['sortOrder'] = sortOrder
