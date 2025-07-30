from enum import Enum, auto


class POSType(Enum):
    S = auto()
    NP = auto()
    VP = auto()
    PP = auto()
    Det = auto()
    Noun = auto()
    Verb = auto()
    Adj = auto()
    Prep = auto()

    @property
    def twaddle_name(self):
        # Only terminal types have twaddle names
        mapping = {
            POSType.Noun: "noun",
            POSType.Verb: "verb",
            POSType.Adj: "adj",
            POSType.Det: "det",
            POSType.Prep: "prep",
        }
        return mapping.get(self, None)
