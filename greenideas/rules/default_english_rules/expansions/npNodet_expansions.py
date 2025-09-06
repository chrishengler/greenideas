from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
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
                DefaultEnglishAttributeType.ANIMACY: INHERIT,
                DefaultEnglishAttributeType.CASE: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
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
                DefaultEnglishAttributeType.ANIMACY: INHERIT,
                DefaultEnglishAttributeType.CASE: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
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
                DefaultEnglishAttributeType.ANIMACY: INHERIT,
                DefaultEnglishAttributeType.CASE: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
            },
        ),
    ],
    weight=0.2,
)

# NP_NoDet -> N RelClause
npNodet__n_relclause_no_commas = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.NP_NoDet),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Noun,
            {
                DefaultEnglishAttributeType.ANIMACY: INHERIT,
                DefaultEnglishAttributeType.CASE: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.RelClause,
            {
                DefaultEnglishAttributeType.ANIMACY: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
    ],
    weight=0.2,
)

# NP_NoDet -> N, RelClause,
npNodet__n_relclause_commas = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.NP_NoDet),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Noun,
            {
                DefaultEnglishAttributeType.ANIMACY: INHERIT,
                DefaultEnglishAttributeType.CASE: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.RelClause,
            {
                DefaultEnglishAttributeType.ANIMACY: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
            pre_punctuation=",",
            post_punctuation=",",
        ),
    ],
    weight=0.2,
)


npNodet_expansions = [
    npNodet__n,
    np_nodet__adjp_np_nodet,
    npNodet__adjp_n,
    npNodet__n_relclause_no_commas,
    npNodet__n_relclause_commas,
]
