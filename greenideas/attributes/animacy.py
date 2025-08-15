from enum import Enum, auto


class Animacy(Enum):
    ANIMATE = auto()
    INANIMATE = auto()

    def __str__(self) -> str:
        return self.name.lower()
