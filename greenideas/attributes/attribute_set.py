from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Self

from greenideas.attributes.attribute_type import AttributeType


@dataclass
class AttributeSet:
    _values: Dict[AttributeType, Any] = field(default_factory=dict)

    def get(self, attr: AttributeType) -> Optional[Any]:
        return self._values.get(attr)

    def set(self, attr: AttributeType, value: Any):
        if not isinstance(value, attr.value_type):
            raise TypeError(
                f"Value for {attr.name} must be of type {attr.value_type.__name__}, got {type(value).__name__}"
            )
        self._values[attr] = value

    def merge(self, other: Self, overwrite: bool = False) -> Self:
        result = AttributeSet()
        for attr, value in self._values.items():
            result._values[attr] = value
        for attr, value in other._values.items():
            if overwrite or attr not in result._values:
                result._values[attr] = value
        return result

    def __contains__(self, attr: AttributeType) -> bool:
        return attr in self._values
