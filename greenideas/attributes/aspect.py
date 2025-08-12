from enum import Enum, auto


class Aspect(Enum):
    SIMPLE = auto()
    PROGRESSIVE = auto()
    PERFECT = auto()
    PERFECT_PROGRESSIVE = auto()

    def __str__(self) -> str:
        return self.name.lower()
