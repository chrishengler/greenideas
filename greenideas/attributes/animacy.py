from enum import auto

from greenideas.attributes.grammatical_attribute import GrammaticalAttribute


class Animacy(GrammaticalAttribute):
    ANIMATE = auto()
    INANIMATE = auto()

    def __str__(self) -> str:
        return self.name.lower()
