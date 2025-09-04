from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.expansion_spec import ExpansionSpec


class GrammarRule:
    def __init__(
        self,
        source: ExpansionSpec,
        expansion: list[ExpansionSpec],
        weight: float = 1.0,
        ignore_after_depth: int = 0,
    ):
        self.source = source
        self.pos = source.pos_type
        self.source_constraints = source.attribute_constraints
        self.expansion = expansion
        self.weight = weight
        self.ignore_after_depth = ignore_after_depth

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
        if self.ignore_after_depth and node.depth >= self.ignore_after_depth:
            return False
        return True
