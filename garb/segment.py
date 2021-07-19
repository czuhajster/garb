

class DynamicSegment (dict):

    def __init__(self,
                 name: str,
                 userSegment: SegmentDefinition,
                 sessionSegment: SegmentDefinition):
        self['name'] = name
        self['userSegment'] = userSegment
        self['sessionSegment'] = sessionSegment

class SegmentDefinition (dict):
    def __init__(self,
                 segmentFilters: list[SegmentFilter]):
