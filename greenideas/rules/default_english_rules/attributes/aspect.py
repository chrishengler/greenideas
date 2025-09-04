from enum import auto

from greenideas.attributes.grammatical_attribute import GrammaticalAttribute


class Aspect(GrammaticalAttribute):
    SIMPLE = auto()
    PROGRESSIVE = auto()
    PERFECT = auto()
    PERFECT_PROGRESSIVE = auto()

    def __str__(self) -> str:
        return self.name.lower()
