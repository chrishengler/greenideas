# NP -> Det NP_NoDet
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.npform import NPForm
from greenideas.rules.default_english_rules.attributes.number import Number
from greenideas.rules.default_english_rules.attributes.person import Person
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

np__det_npNodet = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.NP,
        {
            DefaultEnglishAttributeType.NPFORM: [NPForm.FREE, NPForm.LEXICAL],
            DefaultEnglishAttributeType.PERSON: Person.THIRD,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Det,
            {
                DefaultEnglishAttributeType.CASE: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP_NoDet,
            {
                DefaultEnglishAttributeType.ANIMACY: INHERIT,
                DefaultEnglishAttributeType.CASE: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
    ],
)

# NP_Pl -> NPNoDet
npPl__npNoDet = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.NP,
        {
            DefaultEnglishAttributeType.NUMBER: Number.PLURAL,
            DefaultEnglishAttributeType.NPFORM: [NPForm.FREE, NPForm.LEXICAL],
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.NP_NoDet,
            {
                DefaultEnglishAttributeType.ANIMACY: INHERIT,
                DefaultEnglishAttributeType.CASE: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        )
    ],
)

# NP -> Pron
np__pron = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.NP,
        {DefaultEnglishAttributeType.NPFORM: [NPForm.FREE, NPForm.PRONOMINAL]},
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Pron,
            {
                DefaultEnglishAttributeType.ANIMACY: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.CASE: INHERIT,
            },
        )
    ],
    weight=0.2,
)

np_expansions = [
    np__det_npNodet,
    npPl__npNoDet,
    np__pron,
]
