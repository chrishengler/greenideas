from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.pos_types import POSType

POSTYPE_ATTRIBUTE_MAP = {
    POSType.S: {AttributeType.TENSE, AttributeType.NUMBER, AttributeType.PERSON},
    POSType.NP: {AttributeType.CASE, AttributeType.NUMBER, AttributeType.PERSON},
    POSType.NP_NoDet: {AttributeType.CASE, AttributeType.NUMBER, AttributeType.PERSON},
    POSType.PP: {},
    POSType.VP: {AttributeType.TENSE, AttributeType.NUMBER, AttributeType.PERSON},
    POSType.VP_Bare: {},
    POSType.Adj: set(),
    POSType.Adv: set(),
    POSType.Aux_do: {
        AttributeType.TENSE,
        AttributeType.NUMBER,
        AttributeType.PERSON,
    },
    POSType.Aux_finite: {
        AttributeType.TENSE,
        AttributeType.NUMBER,
        AttributeType.PERSON,
    },
    POSType.Det: {AttributeType.NUMBER, AttributeType.CASE},
    POSType.Noun: {AttributeType.NUMBER, AttributeType.CASE},
    POSType.Prep: set(),
    POSType.Pron: {AttributeType.NUMBER, AttributeType.PERSON, AttributeType.CASE},
    POSType.Verb: {AttributeType.TENSE, AttributeType.PERSON, AttributeType.NUMBER},
    POSType.Verb_Bare: {},
}
