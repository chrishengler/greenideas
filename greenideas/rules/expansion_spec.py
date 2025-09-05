from typing import Any, Optional

from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.pos_type_base import POSType


class InheritSentinel:
    def __repr__(self):
        return "INHERIT"


INHERIT = InheritSentinel()


class ExpansionSpec:
    def __init__(
        self,
        pos_type: POSType,
        attribute_constraints: dict[AttributeType, Any] = None,
        space_follows: bool = True,
        pre_punctuation: Optional[str] = None,
        post_punctuation: Optional[str] = None,
    ):
        self.pos_type = pos_type
        self.attribute_constraints = attribute_constraints or {}
        self.space_follows = space_follows
        self.pre_punctuation = pre_punctuation
        self.post_punctuation = post_punctuation

    def get_constraint(self, attr_type: AttributeType) -> Optional[dict]:
        return self.attribute_constraints.get(attr_type, None)

    def __repr__(self):
        return f"ExpansionSpec({self.pos_type}, {self.attribute_constraints})"

    def __str__(self):
        return f"ExpansionSpec(pos_type={self.pos_type}, attribute_constraints={self.attribute_constraints})"
