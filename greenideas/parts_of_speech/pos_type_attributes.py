from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.pos_types import POSType

POSTYPE_ATTRIBUTE_MAP = {
    POSType.S: {
        AttributeType.ANIMACY,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.TENSE,
    },
    POSType.AdjP: set(),
    POSType.AdvP: set(),
    POSType.AuxP: {
        AttributeType.ASPECT,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.TENSE,
    },
    POSType.Be: {
        AttributeType.ASPECT,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.TENSE,
    },
    POSType.ModalP: {
        AttributeType.ASPECT,
        AttributeType.TENSE,
    },
    POSType.NP: {
        AttributeType.ANIMACY,
        AttributeType.CASE,
        AttributeType.NUMBER,
        AttributeType.PERSON,
    },
    POSType.NP_NoDet: {
        AttributeType.ANIMACY,
        AttributeType.CASE,
        AttributeType.NUMBER,
        AttributeType.PERSON,
    },
    POSType.PP: {},
    POSType.RelClause: {
        AttributeType.ANIMACY,
    },
    POSType.VP: {
        AttributeType.ANIMACY,
        AttributeType.ASPECT,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.TENSE,
        AttributeType.VALENCY,
    },
    POSType.VP_AfterModal: {
        AttributeType.ASPECT,
        AttributeType.VALENCY,
    },
    POSType.VP_Bare: {
        AttributeType.VALENCY,
    },
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
    POSType.Det: {
        AttributeType.CASE,
        AttributeType.NUMBER,
    },
    POSType.Modal: {
        AttributeType.ASPECT,
        AttributeType.TENSE,
    },
    POSType.Noun: {
        AttributeType.ANIMACY,
        AttributeType.CASE,
        AttributeType.NUMBER,
    },
    POSType.Prep: set(),
    POSType.Pron: {
        AttributeType.ANIMACY,
        AttributeType.CASE,
        AttributeType.NUMBER,
        AttributeType.PERSON,
    },
    POSType.RelativePron: {
        AttributeType.ANIMACY,
    },
    POSType.Subordinator: set(),
    POSType.Verb: {
        AttributeType.ANIMACY,
        AttributeType.ASPECT,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.TENSE,
        AttributeType.VALENCY,
    },
    POSType.Verb_AfterModal: {
        AttributeType.ASPECT,
        AttributeType.VALENCY,
    },
    POSType.Verb_Bare: {AttributeType.VALENCY},
}


def relevant_attributes(pos_type: POSType) -> set[AttributeType]:
    if pos_type not in POSTYPE_ATTRIBUTE_MAP:
        raise ValueError(f"No relevant attributes specified for POSType: {pos_type}")
    return POSTYPE_ATTRIBUTE_MAP[pos_type]
