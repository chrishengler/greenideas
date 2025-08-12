from enum import Enum, auto


class POSType(Enum):
    S = auto()

    AdjP = auto()
    AdvP = auto()
    AuxP = auto()
    NP = auto()
    NP_NoDet = auto()
    PP = auto()
    VP = auto()
    VP_Bare = auto()

    Adj = auto()
    Adv = auto()
    Aux_do = auto()  # do support
    Aux_finite = auto()  # tensed auxiliaries, have/be
    Be = auto()
    Conj = auto()
    Det = auto()
    Noun = auto()
    Prep = auto()
    Pron = auto()
    Verb = auto()
    Verb_Bare = auto()
