from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.default_english_pos_types import DefaultEnglishPOSType

POSTYPE_ATTRIBUTE_MAP = {
    DefaultEnglishPOSType.S: {
        AttributeType.ANIMACY,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.TENSE,
        AttributeType.VOICE,
    },
    DefaultEnglishPOSType.AdjP: set(),
    DefaultEnglishPOSType.AdvP: set(),
    DefaultEnglishPOSType.AuxP: {
        AttributeType.ASPECT,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.TENSE,
    },
    DefaultEnglishPOSType.Be: {
        AttributeType.ASPECT,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.TENSE,
    },
    DefaultEnglishPOSType.ModalP: {
        AttributeType.ASPECT,
        AttributeType.TENSE,
    },
    DefaultEnglishPOSType.NP: {
        AttributeType.ANIMACY,
        AttributeType.CASE,
        AttributeType.NPFORM,
        AttributeType.NUMBER,
        AttributeType.PERSON,
    },
    DefaultEnglishPOSType.NP_NoDet: {
        AttributeType.ANIMACY,
        AttributeType.CASE,
        AttributeType.NUMBER,
        AttributeType.PERSON,
    },
    DefaultEnglishPOSType.PP: {},
    DefaultEnglishPOSType.RelClause: {
        AttributeType.ANIMACY,
        AttributeType.NUMBER,
        AttributeType.PERSON,
    },
    DefaultEnglishPOSType.VP: {
        AttributeType.ANIMACY,
        AttributeType.ASPECT,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.TENSE,
        AttributeType.VALENCY,
        AttributeType.VOICE,
    },
    DefaultEnglishPOSType.VP_AfterModal: {
        AttributeType.ASPECT,
    },
    DefaultEnglishPOSType.VP_Bare: {
        AttributeType.VALENCY,
    },
    DefaultEnglishPOSType.VP_Passive: {
        AttributeType.ASPECT,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.TENSE,
        AttributeType.VALENCY,
    },
    DefaultEnglishPOSType.Adj: set(),
    DefaultEnglishPOSType.Adv: set(),
    DefaultEnglishPOSType.Aux_do: {
        AttributeType.TENSE,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.ASPECT,
    },
    DefaultEnglishPOSType.Aux_finite: {
        AttributeType.TENSE,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.ASPECT,
    },
    DefaultEnglishPOSType.CoordConj: set(),
    DefaultEnglishPOSType.Det: {
        AttributeType.CASE,
        AttributeType.NUMBER,
    },
    DefaultEnglishPOSType.Deg: set(),
    DefaultEnglishPOSType.Modal: {
        AttributeType.ASPECT,
        AttributeType.TENSE,
    },
    DefaultEnglishPOSType.Noun: {
        AttributeType.ANIMACY,
        AttributeType.CASE,
        AttributeType.NUMBER,
    },
    DefaultEnglishPOSType.Prep: set(),
    DefaultEnglishPOSType.Pron: {
        AttributeType.ANIMACY,
        AttributeType.CASE,
        AttributeType.NUMBER,
        AttributeType.PERSON,
    },
    DefaultEnglishPOSType.RelativePron: {
        AttributeType.ANIMACY,
    },
    DefaultEnglishPOSType.SimpleConj: set(),
    DefaultEnglishPOSType.Subordinator: set(),
    DefaultEnglishPOSType.Verb: {
        AttributeType.ANIMACY,
        AttributeType.ASPECT,
        AttributeType.NUMBER,
        AttributeType.PERSON,
        AttributeType.TENSE,
        AttributeType.VALENCY,
        AttributeType.VOICE,
    },
    DefaultEnglishPOSType.Verb_AfterModal: {
        AttributeType.ASPECT,
        AttributeType.VALENCY,
    },
    DefaultEnglishPOSType.Verb_Bare: {AttributeType.VALENCY},
}


def relevant_attributes(pos_type: DefaultEnglishPOSType) -> set[AttributeType]:
    if pos_type not in POSTYPE_ATTRIBUTE_MAP:
        raise ValueError(f"No relevant attributes specified for POSType: {pos_type}")
    return POSTYPE_ATTRIBUTE_MAP[pos_type]
