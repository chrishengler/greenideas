from typing import Any

from greenideas.attributes.attribute_type import AttributeType
from greenideas.pos_types import POSType


class InheritSentinel:
    def __repr__(self):
        return "INHERIT"


INHERIT = InheritSentinel()


class ExpansionSpec:
    def __init__(
        self, pos_type: POSType, attribute_constraints: dict[AttributeType, Any] = None
    ):
        """
        Args:
            pos_type: The POS type for this child
            attribute_constraints: Dict of AttributeType to value, INHERIT, or None
        """
        self.pos_type = pos_type
        self.attribute_constraints = (
            attribute_constraints or {}
        )  # e.g. {AttributeType.NUMBER: INHERIT, AttributeType.CASE: Gen}

    def get_constraint(self, attr_type):
        return self.attribute_constraints.get(attr_type, None)

    def __repr__(self):
        return f"ExpansionSpec({self.pos_type}, {self.attribute_constraints})"
