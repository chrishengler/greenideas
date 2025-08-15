from enum import Enum, auto


class Valency(Enum):
    MONOVALENT = auto()
    DIVALENT = auto()
    # TRIVALENT = auto()  # handling trivalent verbs will require twaddle labels
    # twaddle labels will be handled as part of forthcoming pronoun update

    def __str__(self) -> str:
        return self.name.lower()
