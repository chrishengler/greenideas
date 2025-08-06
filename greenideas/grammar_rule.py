from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import ExpansionSpec


class GrammarRule:
    def __init__(
        self,
        part_of_speech: POSType,
        expansion: list[ExpansionSpec],
        weight: float = 1.0,
    ):
        self.part_of_speech = part_of_speech
        self.expansion = expansion
        self.weight = weight

    def get_child_spec(self, idx: int) -> ExpansionSpec:
        return self.expansion[idx]

    def __repr__(self):
        return f"{self.part_of_speech} -> [{('; '.join(str(item) for item in self.expansion))}]"
