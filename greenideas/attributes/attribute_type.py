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
        self.attr_name = attr_name
        self.value_type = value_type

    def __str__(self) -> str:
        return self.attr_name
