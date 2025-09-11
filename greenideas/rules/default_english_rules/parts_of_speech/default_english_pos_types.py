from enum import auto

from greenideas.parts_of_speech.pos_type_base import POSType


class DefaultEnglishPOSType(POSType):
    Utterance = auto()

    S = auto()
    Q = auto()

    AdjP = auto()
    AdvP = auto()
    AuxP = auto()
    ModalP = auto()
    NP = auto()
    NP_NoDet = auto()
    PP = auto()
    RelClause = auto()
    VP = auto()
    VP_AfterFrontedAux = auto()
    VP_AfterModal = auto()
    VP_Bare = auto()
    VP_Passive = auto()

    Adj = auto()
    Adv = auto()
    Aux_do = auto()  # do support
    Aux_finite = auto()  # tensed auxiliaries, have/be
    Be = auto()
    CoordConj = auto()
    Det = auto()
    Deg = auto()
    Modal = auto()
    Noun = auto()
    Prep = auto()
    Pron = auto()
    RelativePron = auto()
    SimpleConj = auto()
    Subordinator = auto()
    Verb = auto()
    Verb_AfterModal = auto()
    Verb_Bare = auto()
