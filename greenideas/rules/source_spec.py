from typing import Any, Optional

from greenideas.attributes.attribute_type import AttributeType
from greenideas.exceptions import InvalidGrammarRule
from greenideas.parts_of_speech.pos_type_attributes import POSTYPE_ATTRIBUTE_MAP
from greenideas.parts_of_speech.pos_types import POSType


class SourceSpec:
    def __init__(
        self, pos_type: POSType, attribute_constraints: dict[AttributeType, Any] = None
    ):
        self.pos_type = pos_type
        self.attribute_constraints = attribute_constraints or {}
        for attr, val in self.attribute_constraints.items():
            if attr not in POSTYPE_ATTRIBUTE_MAP[pos_type]:
                raise InvalidGrammarRule(
                    f"SourceSpec includes constraints on {str(attr)}, not defined as relevant attribute for {pos_type}"
                )
            if not isinstance(val, attr.value_type):
                if isinstance(val, list) and all(
                    isinstance(v, attr.value_type) for v in val
                ):
                    continue
                raise TypeError(
                    f"Value for {attr.name} must be of type {str(attr)} (or list of), got {type(val)}"
                )

    def get_constraint(self, attr_type: AttributeType) -> Optional[dict]:
        return self.attribute_constraints.get(attr_type, None)

    def __repr__(self):
        return f"SourceSpec({self.pos_type}, {self.attribute_constraints})"
