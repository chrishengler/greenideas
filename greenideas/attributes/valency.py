from enum import Enum, auto


class Valency(Enum):
    MONOVALENT = auto()
    DIVALENT = auto()
    TRIVALENT = auto()

    def __str__(self) -> str:
        return self.name.lower()
