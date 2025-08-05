from dataclasses import dataclass, field
from typing import List, Self

from greenideas.attributes.attribute_set import AttributeSet
from greenideas.exceptions import RelevantAttributesNotSpecified
from greenideas.parts_of_speech.pos_type_attributes import POSTYPE_ATTRIBUTE_MAP
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

    @property
    def relevant_attributes(self) -> AttributeSet:
        """Return attributes that are relevant for this node."""
        if self.type not in POSTYPE_ATTRIBUTE_MAP:
            raise RelevantAttributesNotSpecified(
                f"No relevant attributes specified for POSType: {self.type}"
            )
        return POSTYPE_ATTRIBUTE_MAP.get(self.type, set())
