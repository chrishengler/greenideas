from greenideas.expansion_spec import ExpansionSpec
from greenideas.pos_types import POSType


class GrammarRule:
    def __init__(
        self,
        part_of_speech: POSType,
        expansion: list[ExpansionSpec],
        weight: float = 1.0,
    ):
        """
        Args:
            part_of_speech: The parent POS type
            expansion: List of ExpansionSpec objects for each child
            weight: Rule weight
        """
        self.part_of_speech = part_of_speech
        self.expansion = expansion  # List of ExpansionSpec
        self.weight = weight

    def get_child_spec(self, idx: int) -> ExpansionSpec:
        return self.expansion[idx]

    def __repr__(self):
        return f"{self.part_of_speech} -> [{('; '.join(str(item) for item in self.expansion))}]"
