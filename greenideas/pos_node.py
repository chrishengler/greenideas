from dataclasses import dataclass, field
from typing import List, Optional

from .attributes.attribute_set import AttributeSet
from .pos_types import POSType


@dataclass
class POSNode:
    type: POSType
    children: List["POSNode"] = field(default_factory=list)
    value: Optional[str] = None
    attributes: AttributeSet = field(default_factory=AttributeSet)

    def __str__(self):
        children = (
            f"[{", ".join(str(child) for child in self.children)}]"
            if self.children
            else None
        )
        return f"{self.type.name}{children if children else ""}"

    def resolve(self):
        # If terminal, return the twaddle tag or value
        if self.type.twaddle_name:
            return f"<{self.type.twaddle_name}>"
        if self.value is not None:
            return str(self.value)
        # Otherwise, recursively resolve children
        return " ".join(child.resolve() for child in self.children)
