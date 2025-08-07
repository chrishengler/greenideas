from dataclasses import dataclass, field
from typing import List, Self

from greenideas.attributes.attribute_set import AttributeSet
from greenideas.parts_of_speech.pos_types import POSType


@dataclass
class POSNode:
    type: POSType
    children: List[Self] = field(default_factory=list)
    attributes: AttributeSet = field(default_factory=AttributeSet)

    def __str__(self):
        children = (
            f"[{', '.join(str(child) for child in self.children)}]"
            if self.children
            else None
        )
        return f"{self.type.name}{children if children else ''}"
