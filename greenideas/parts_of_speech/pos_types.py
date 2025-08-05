from enum import Enum, auto


class POSType(Enum):
    S = auto()
    NP = auto()
    NP_NoDet = auto()
    PP = auto()
    VP = auto()
    VP_Bare = auto()

    Adj = auto()
    Adv = auto()
    Aux_do = auto()  # do support
    Aux_finite = auto()  # tensed auxiliaries, have/be
    Det = auto()
    Noun = auto()
    Prep = auto()
    Verb = auto()
    Verb_Bare = auto()

    @property
    def twaddle_name(self) -> str:
        # Only terminal types have twaddle names
        mapping = {
            POSType.Adj: "adj",
            POSType.Adv: "adv",
            POSType.Aux_do: "aux",
            POSType.Aux_finite: "aux",
            POSType.Det: "det",
            POSType.Noun: "noun",
            POSType.Prep: "prep",
            POSType.Verb: "verb",
            POSType.Verb_Bare: "verb",
        }
        return mapping.get(self)
