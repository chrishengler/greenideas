from enum import Enum
from typing import Type

from greenideas.attributes.case import Case
from greenideas.attributes.number import Number
from greenideas.attributes.person import Person
from greenideas.attributes.tense import Tense


class AttributeType(Enum):
    PERSON = ("person", Person)
    NUMBER = ("number", Number)
    TENSE = ("tense", Tense)
    CASE = ("case", Case)

    def __init__(self, attr_name: str, value_type: Type):
        self.name = attr_name  # Changed from name to attr_name
        self.value_type = (
            value_type  # No need for lazy loading since we're using direct references
        )

    def __str__(self) -> str:
        return self.name
