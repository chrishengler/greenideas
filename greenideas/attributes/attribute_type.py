from enum import Enum
from typing import Type


class AttributeType(Enum):
    def __init__(self, attr_name: str, value_type: Type):
        self.attr_name = attr_name
        self.value_type = value_type

    def __str__(self) -> str:
        return self.attr_name
