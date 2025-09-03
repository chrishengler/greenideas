# NP -> Det NP_NoDet
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.npform import NPForm
from greenideas.attributes.number import Number
from greenideas.attributes.person import Person
from greenideas.parts_of_speech.default_english_pos_types import DefaultEnglishPOSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

np__det_npNodet = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.NP,
        {
            AttributeType.NPFORM: [NPForm.FREE, NPForm.LEXICAL],
            AttributeType.PERSON: Person.THIRD,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Det,
            {
                AttributeType.CASE: INHERIT,
                AttributeType.NUMBER: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP_NoDet,
            {
                AttributeType.ANIMACY: INHERIT,
                AttributeType.CASE: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
    ],
)

# NP_Pl -> NPNoDet
npPl__npNoDet = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.NP,
        {
            AttributeType.NUMBER: Number.PLURAL,
            AttributeType.NPFORM: [NPForm.FREE, NPForm.LEXICAL],
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.NP_NoDet,
            {
                AttributeType.ANIMACY: INHERIT,
                AttributeType.CASE: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        )
    ],
)

# NP -> Pron
np__pron = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.NP,
        {AttributeType.NPFORM: [NPForm.FREE, NPForm.PRONOMINAL]},
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Pron,
            {
                AttributeType.ANIMACY: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.CASE: INHERIT,
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
