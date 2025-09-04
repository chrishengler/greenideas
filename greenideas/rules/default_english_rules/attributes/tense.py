from enum import auto

from greenideas.attributes.grammatical_attribute import GrammaticalAttribute


class Tense(GrammaticalAttribute):
    PRESENT = auto()
    PAST = auto()
