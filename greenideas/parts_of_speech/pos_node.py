from dataclasses import dataclass, field
from typing import List, Self

from greenideas.attributes.attribute_set import AttributeSet
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)


@dataclass
class POSNode:
    type: DefaultEnglishPOSType
    children: List[Self] = field(default_factory=list)
    attributes: AttributeSet = field(default_factory=AttributeSet)
    depth: int = 0

    def __str__(self):
        children = (
            f"[{', '.join(str(child) for child in self.children)}]"
            if self.children
            else None
        )
        return f"{self.type.name}:{children if children else ''}"
