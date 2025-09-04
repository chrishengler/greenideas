from typing import Any, Optional

from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.pos_type_base import POSType


class SourceSpec:
    def __init__(
        self,
        pos_type: POSType,
        attribute_constraints: dict[AttributeType, Any] = None,
    ):
        self.pos_type = pos_type
        self.attribute_constraints = attribute_constraints or {}

    def get_constraint(self, attr_type: AttributeType) -> Optional[dict]:
        return self.attribute_constraints.get(attr_type, None)

    def __repr__(self):
        return f"SourceSpec({self.pos_type}, {self.attribute_constraints})"
