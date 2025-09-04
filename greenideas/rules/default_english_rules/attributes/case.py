from enum import auto

from greenideas.attributes.grammatical_attribute import GrammaticalAttribute


class Case(GrammaticalAttribute):
    NOMINATIVE = auto()
    OBJECTIVE = auto()
    GENITIVE = auto()
