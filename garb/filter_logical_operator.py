"""FilterLogicalOperator module

This module defines the FilterLogicalOperator object.
"""

from enum import Enum

class FilterLogicalOperator (Enum):
    """A FilterLogicalOperator object.
    """

    OR = "OR",
    AND = "AND",
    OPERATOR_UNSPECIFIED = "OR"
