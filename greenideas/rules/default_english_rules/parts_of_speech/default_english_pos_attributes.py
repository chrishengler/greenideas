from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)

POSTYPE_ATTRIBUTE_MAP = {
    DefaultEnglishPOSType.Utterance: {DefaultEnglishAttributeType.MOOD},
    DefaultEnglishPOSType.S: {
        DefaultEnglishAttributeType.ANIMACY,
        DefaultEnglishAttributeType.NUMBER,
        DefaultEnglishAttributeType.PERSON,
        DefaultEnglishAttributeType.TENSE,
        DefaultEnglishAttributeType.VOICE,
    },
    DefaultEnglishPOSType.Q: {
        DefaultEnglishAttributeType.ANIMACY,
        DefaultEnglishAttributeType.ASPECT,
        DefaultEnglishAttributeType.NUMBER,
        DefaultEnglishAttributeType.PERSON,
        DefaultEnglishAttributeType.TENSE,
        DefaultEnglishAttributeType.VOICE,
    },
    DefaultEnglishPOSType.AdjP: set(),
    DefaultEnglishPOSType.AdvP: set(),
    DefaultEnglishPOSType.AuxP: {
        DefaultEnglishAttributeType.ASPECT,
        DefaultEnglishAttributeType.NUMBER,
        DefaultEnglishAttributeType.PERSON,
        DefaultEnglishAttributeType.TENSE,
    },
    DefaultEnglishPOSType.Be: {
        DefaultEnglishAttributeType.ASPECT,
        DefaultEnglishAttributeType.NUMBER,
        DefaultEnglishAttributeType.PERSON,
        DefaultEnglishAttributeType.TENSE,
    },
    DefaultEnglishPOSType.ModalP: {
        DefaultEnglishAttributeType.ASPECT,
        DefaultEnglishAttributeType.TENSE,
    },
    DefaultEnglishPOSType.NP: {
        DefaultEnglishAttributeType.ANIMACY,
        DefaultEnglishAttributeType.CASE,
        DefaultEnglishAttributeType.NPFORM,
        DefaultEnglishAttributeType.NUMBER,
        DefaultEnglishAttributeType.PERSON,
    },
    DefaultEnglishPOSType.NP_NoDet: {
        DefaultEnglishAttributeType.ANIMACY,
        DefaultEnglishAttributeType.CASE,
        DefaultEnglishAttributeType.NUMBER,
        DefaultEnglishAttributeType.PERSON,
    },
    DefaultEnglishPOSType.PP: {},
    DefaultEnglishPOSType.RelClause: {
        DefaultEnglishAttributeType.ANIMACY,
        DefaultEnglishAttributeType.NUMBER,
        DefaultEnglishAttributeType.PERSON,
    },
    DefaultEnglishPOSType.VP: {
        DefaultEnglishAttributeType.ANIMACY,
        DefaultEnglishAttributeType.ASPECT,
        DefaultEnglishAttributeType.NUMBER,
        DefaultEnglishAttributeType.PERSON,
        DefaultEnglishAttributeType.TENSE,
        DefaultEnglishAttributeType.VALENCY,
        DefaultEnglishAttributeType.VOICE,
    },
    DefaultEnglishPOSType.VP_AfterModal: {
        DefaultEnglishAttributeType.ASPECT,
    },
    DefaultEnglishPOSType.VP_Bare: {
        DefaultEnglishAttributeType.VALENCY,
    },
    DefaultEnglishPOSType.VP_Passive: {
        DefaultEnglishAttributeType.ASPECT,
        DefaultEnglishAttributeType.NUMBER,
        DefaultEnglishAttributeType.PERSON,
        DefaultEnglishAttributeType.TENSE,
        DefaultEnglishAttributeType.VALENCY,
    },
    DefaultEnglishPOSType.Adj: set(),
    DefaultEnglishPOSType.Adv: set(),
    DefaultEnglishPOSType.Aux_do: {
        DefaultEnglishAttributeType.TENSE,
        DefaultEnglishAttributeType.NUMBER,
        DefaultEnglishAttributeType.PERSON,
        DefaultEnglishAttributeType.ASPECT,
    },
    DefaultEnglishPOSType.Aux_finite: {
        DefaultEnglishAttributeType.TENSE,
        DefaultEnglishAttributeType.NUMBER,
        DefaultEnglishAttributeType.PERSON,
        DefaultEnglishAttributeType.ASPECT,
    },
    DefaultEnglishPOSType.CoordConj: set(),
    DefaultEnglishPOSType.Det: {
        DefaultEnglishAttributeType.CASE,
        DefaultEnglishAttributeType.NUMBER,
    },
    DefaultEnglishPOSType.Deg: set(),
    DefaultEnglishPOSType.Modal: {
        DefaultEnglishAttributeType.ASPECT,
        DefaultEnglishAttributeType.TENSE,
    },
    DefaultEnglishPOSType.Noun: {
        DefaultEnglishAttributeType.ANIMACY,
        DefaultEnglishAttributeType.CASE,
        DefaultEnglishAttributeType.NUMBER,
    },
    DefaultEnglishPOSType.Prep: set(),
    DefaultEnglishPOSType.Pron: {
        DefaultEnglishAttributeType.ANIMACY,
        DefaultEnglishAttributeType.CASE,
        DefaultEnglishAttributeType.NUMBER,
        DefaultEnglishAttributeType.PERSON,
    },
    DefaultEnglishPOSType.RelativePron: {
        DefaultEnglishAttributeType.ANIMACY,
    },
    DefaultEnglishPOSType.SimpleConj: set(),
    DefaultEnglishPOSType.Subordinator: set(),
    DefaultEnglishPOSType.Verb: {
        DefaultEnglishAttributeType.ANIMACY,
        DefaultEnglishAttributeType.ASPECT,
        DefaultEnglishAttributeType.NUMBER,
        DefaultEnglishAttributeType.PERSON,
        DefaultEnglishAttributeType.TENSE,
        DefaultEnglishAttributeType.VALENCY,
        DefaultEnglishAttributeType.VOICE,
    },
    DefaultEnglishPOSType.Verb_AfterModal: {
        DefaultEnglishAttributeType.ASPECT,
        DefaultEnglishAttributeType.VALENCY,
    },
    DefaultEnglishPOSType.VP_AfterFrontedAux: {
        DefaultEnglishAttributeType.ASPECT,
        DefaultEnglishAttributeType.TENSE,
        DefaultEnglishAttributeType.VALENCY,
        DefaultEnglishAttributeType.VOICE,
    },
    DefaultEnglishPOSType.Verb_Bare: {DefaultEnglishAttributeType.VALENCY},
}


def relevant_attributes(
    pos_type: DefaultEnglishPOSType,
) -> set[DefaultEnglishAttributeType]:
    if pos_type not in POSTYPE_ATTRIBUTE_MAP:
        raise ValueError(f"No relevant attributes specified for POSType: {pos_type}")
    return POSTYPE_ATTRIBUTE_MAP[pos_type]
