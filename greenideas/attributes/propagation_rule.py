from dataclasses import dataclass
from typing import Set

from greenideas.attributes.attribute_type import AttributeType
from greenideas.pos_types import POSType


@dataclass
class PropagationRule:
    """Defines how attributes should propagate from one node type to another."""

    source_type: POSType
    target_type: POSType
    attributes: Set[AttributeType]

    def __str__(self):
        return f"{self.source_type.name} -> {self.target_type.name}: propagate {self.attributes}"
