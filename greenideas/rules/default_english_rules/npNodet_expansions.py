from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# NP_NoDet -> N
npNodet__n = GrammarRule(
    SourceSpec(POSType.NP_NoDet),
    [
        ExpansionSpec(
            POSType.Noun,
            {AttributeType.NUMBER: INHERIT, AttributeType.CASE: INHERIT},
        ),
    ],
)

# NP_NoDet -> AdjP NP_NoDet
np_nodet__adjp_np_nodet = GrammarRule(
    SourceSpec(POSType.NP_NoDet),
    [
        ExpansionSpec(POSType.AdjP),
        ExpansionSpec(
            POSType.NP_NoDet,
            {AttributeType.NUMBER: INHERIT, AttributeType.CASE: INHERIT},
        ),
    ],
    weight=0.2,
)

# NP_NoDet -> AdjP N
npNodet__adjp_n = GrammarRule(
    SourceSpec(POSType.NP_NoDet),
    [
        ExpansionSpec(POSType.AdjP),
        ExpansionSpec(
            POSType.Noun,
            {AttributeType.NUMBER: INHERIT, AttributeType.CASE: INHERIT},
        ),
    ],
    weight=0.2,
)

npNodet_expansions = [
    npNodet__n,
    np_nodet__adjp_np_nodet,
    npNodet__adjp_n,
]
