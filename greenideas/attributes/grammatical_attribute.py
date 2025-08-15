from enum import Enum, unique
from random import choices
from typing import Self


@unique
class GrammaticalAttribute(Enum):

    def __init__(self, label, weight=1):
        self.label = label
        self.weight = weight

    @classmethod
    def random_from(cls, allowed: list[Self]) -> Self:
        weights = [elem.weight for elem in allowed]
        return choices(allowed, weights=weights)[0]
