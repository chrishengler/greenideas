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

    def is_subject(self) -> bool:
        """Determine if this NP is a subject (based on position under S)"""
        if self.type != POSType.NP:
            return False
        parent = self._get_parent()  # You'll need to implement parent tracking
        if not parent or parent.type_ != POSType.S:
            return False
        return parent.children.index(self) == 0  # First NP under S is subject

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
