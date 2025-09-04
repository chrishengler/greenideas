from greenideas.attributes.grammatical_attribute import GrammaticalAttribute


class Valency(GrammaticalAttribute):
    MONOVALENT = ("monovalent", 0.5)
    DIVALENT = ("divalent", 0.3)
    TRIVALENT = ("trivalent", 0.2)

    def __str__(self) -> str:
        return self.name.lower()
