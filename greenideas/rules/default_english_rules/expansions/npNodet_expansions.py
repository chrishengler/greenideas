from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.default_english_pos_types import DefaultEnglishPOSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# NP_NoDet -> N
npNodet__n = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.NP_NoDet),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Noun,
            {
                AttributeType.ANIMACY: INHERIT,
                AttributeType.CASE: INHERIT,
                AttributeType.NUMBER: INHERIT,
            },
        ),
    ],
)

# NP_NoDet -> AdjP NP_NoDet
np_nodet__adjp_np_nodet = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.NP_NoDet),
    [
        ExpansionSpec(DefaultEnglishPOSType.AdjP),
        ExpansionSpec(
            DefaultEnglishPOSType.NP_NoDet,
            {
                AttributeType.ANIMACY: INHERIT,
                AttributeType.CASE: INHERIT,
                AttributeType.NUMBER: INHERIT,
            },
        ),
    ],
    weight=0.2,
)

# NP_NoDet -> AdjP N
npNodet__adjp_n = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.NP_NoDet),
    [
        ExpansionSpec(DefaultEnglishPOSType.AdjP),
        ExpansionSpec(
            DefaultEnglishPOSType.Noun,
            {
                AttributeType.ANIMACY: INHERIT,
                AttributeType.CASE: INHERIT,
                AttributeType.NUMBER: INHERIT,
            },
        ),
    ],
    weight=0.2,
)

# NP_NoDet -> N RelClause
npNodet__n_relclause = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.NP_NoDet),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Noun,
            {
                AttributeType.ANIMACY: INHERIT,
                AttributeType.CASE: INHERIT,
                AttributeType.NUMBER: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.RelClause,
            {
                AttributeType.ANIMACY: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
    ],
    weight=0.2,
)

npNodet_expansions = [
    npNodet__n,
    np_nodet__adjp_np_nodet,
    npNodet__adjp_n,
    npNodet__n_relclause,
]
