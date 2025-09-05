from dataclasses import dataclass, field
from typing import List, Optional, Self

from greenideas.attributes.attribute_set import AttributeSet
from greenideas.parts_of_speech.pos_type_base import POSType


@dataclass
class POSNode:
    type: POSType
    children: List[Self] = field(default_factory=list)
    attributes: AttributeSet = field(default_factory=AttributeSet)
    depth: int = 0
    space_follows: bool = True
    post_punctuation: Optional[str] = None
    pre_punctuation: Optional[str] = None

    def __str__(self):
        children = (
            f"[{', '.join(str(child) for child in self.children)}]"
            if self.children
            else None
        )
        return f"{self.type.name}:{children if children else ''}"
