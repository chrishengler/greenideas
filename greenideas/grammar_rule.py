from greenideas.pos_types import POSType


class GrammarRule:
    def __init__(
        self, part_of_speech: POSType, expansion: POSType, weight: float = 1.0
    ):
        self.part_of_speech = part_of_speech
        self.expansion = expansion
        self.weight = weight
