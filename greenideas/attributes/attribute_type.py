from enum import Enum
from typing import Type

from greenideas.attributes.aspect import Aspect
from greenideas.attributes.case import Case
from greenideas.attributes.number import Number
from greenideas.attributes.person import Person
from greenideas.attributes.tense import Tense


class AttributeType(Enum):
    ASPECT = ("aspect", Aspect)
    CASE = ("case", Case)
    NUMBER = ("number", Number)
    PERSON = ("person", Person)
    TENSE = ("tense", Tense)

    def __init__(self, attr_name: str, value_type: Type):
        self.attr_name = attr_name
        self.value_type = value_type

    def __str__(self) -> str:
        return self.attr_name
