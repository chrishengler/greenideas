from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.pos_types import POSType

POSTYPE_ATTRIBUTE_MAP = {
    POSType.S: {AttributeType.TENSE, AttributeType.NUMBER, AttributeType.PERSON},
    POSType.AdjP: set(),
    POSType.AdvP: set(),
    POSType.AuxP: {
        AttributeType.TENSE,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.ASPECT,
    },
    POSType.Be: {
        AttributeType.TENSE,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.ASPECT,
    },
    POSType.ModalP: {
        AttributeType.TENSE,
        AttributeType.ASPECT,
    },
    POSType.NP: {AttributeType.CASE, AttributeType.NUMBER, AttributeType.PERSON},
    POSType.NP_NoDet: {AttributeType.CASE, AttributeType.NUMBER, AttributeType.PERSON},
    POSType.PP: {},
    POSType.VP: {
        AttributeType.TENSE,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.ASPECT,
    },
    POSType.VP_AfterModal: {
        AttributeType.ASPECT,
    },
    POSType.VP_Bare: {},
    POSType.Adj: set(),
    POSType.Adv: set(),
    POSType.Aux_do: {
        AttributeType.TENSE,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.ASPECT,
    },
    POSType.Aux_finite: {
        AttributeType.TENSE,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.ASPECT,
    },
    POSType.CoordConj: set(),
    POSType.Det: {AttributeType.NUMBER, AttributeType.CASE},
    POSType.Modal: {
        AttributeType.TENSE,
        AttributeType.ASPECT,
    },
    POSType.Noun: {AttributeType.NUMBER, AttributeType.CASE},
    POSType.Prep: set(),
    POSType.Pron: {AttributeType.NUMBER, AttributeType.PERSON, AttributeType.CASE},
    POSType.Subordinator: set(),
    POSType.Verb: {
        AttributeType.TENSE,
        AttributeType.PERSON,
        AttributeType.NUMBER,
        AttributeType.ASPECT,
    },
    POSType.Verb_AfterModal: {
        AttributeType.ASPECT,
    },
    POSType.Verb_Bare: {},
}


def relevant_attributes(pos_type: POSType) -> set[AttributeType]:
    if pos_type not in POSTYPE_ATTRIBUTE_MAP:
        raise ValueError(f"No relevant attributes specified for POSType: {pos_type}")
    return POSTYPE_ATTRIBUTE_MAP[pos_type]
