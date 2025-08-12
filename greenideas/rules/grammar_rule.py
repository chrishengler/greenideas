from greenideas.attributes.attribute_type import AttributeType
from greenideas.exceptions import InvalidGrammarRule
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_type_attributes import relevant_attributes
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec


class GrammarRule:
    def __init__(
        self,
        source: ExpansionSpec,
        expansion: list[ExpansionSpec],
        weight: float = 1.0,
    ):
        self.source = source
        self.pos = source.pos_type
        self.source_constraints = source.attribute_constraints
        self.expansion = expansion
        self.weight = weight

    def validate_attribute_constraint(
        self, pos_type: POSType, attr: AttributeType, value
    ) -> bool:
        if value == INHERIT and attr not in relevant_attributes(pos_type):
            raise InvalidGrammarRule(
                f"Rule {str(self)} requires inheriting {attr} from {pos_type} "
                f"but {attr} is not a relevant attribute for {pos_type}"
            )

    def get_child_spec(self, idx: int) -> ExpansionSpec:
        return self.expansion[idx]

    def __repr__(self):
        sep = "\n\n"
        return f"{self.pos}({self.source_constraints}) -> [{sep.join(str(item) for item in self.expansion)}]"

    def is_applicable_to_node(self, node: POSNode) -> bool:
        for attr_type, constraint in self.source_constraints.items():
            if isinstance(constraint, list):
                if node.attributes.get(attr_type) not in constraint:
                    return False
            elif node.attributes.get(attr_type) != constraint:
                return False
        return True
