from typing import Any, Optional

from greenideas.attributes.attribute_type import AttributeType
from greenideas.exceptions import InvalidGrammarRule
from greenideas.parts_of_speech.pos_type_attributes import relevant_attributes
from greenideas.parts_of_speech.pos_types import POSType


class InheritSentinel:
    def __repr__(self):
        return "INHERIT"


INHERIT = InheritSentinel()


class ExpansionSpec:
    def __init__(
        self, pos_type: POSType, attribute_constraints: dict[AttributeType, Any] = None
    ):
        self.pos_type = pos_type
        self.attribute_constraints = attribute_constraints or {}
        for attr in self.attribute_constraints:
            if attr not in relevant_attributes(self.pos_type):
                raise InvalidGrammarRule(
                    f"Attribute constraints on {attr}, not defined as relevant attribute for {pos_type}"
                )

    def get_constraint(self, attr_type: AttributeType) -> Optional[dict]:
        return self.attribute_constraints.get(attr_type, None)

    def __repr__(self):
        return f"ExpansionSpec({self.pos_type}, {self.attribute_constraints})"

    def __str__(self):
        return f"ExpansionSpec(pos_type={self.pos_type}, attribute_constraints={self.attribute_constraints})"
