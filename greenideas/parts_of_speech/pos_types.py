from enum import Enum, auto


class POSType(Enum):
    S = auto()

    AdjP = auto()
    AdvP = auto()
    AuxP = auto()
    ModalP = auto()
    NP = auto()
    NP_NoDet = auto()
    PP = auto()
    RelClause = auto()
    VP = auto()
    VP_AfterModal = auto()
    VP_Bare = auto()

    Adj = auto()
    Adv = auto()
    Aux_do = auto()  # do support
    Aux_finite = auto()  # tensed auxiliaries, have/be
    Be = auto()
    CoordConj = auto()
    Det = auto()
    Modal = auto()
    Noun = auto()
    Prep = auto()
    Pron = auto()
    RelativePron = auto()
    Subordinator = auto()
    Verb = auto()
    Verb_AfterModal = auto()
    Verb_Bare = auto()
