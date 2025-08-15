from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.attributes.valency import Valency
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# VP -> VP AdvP
vp__vp_advp = GrammarRule(
    SourceSpec(POSType.VP),
    [
        ExpansionSpec(
            POSType.VP,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VALENCY: INHERIT,
            },
        ),
        ExpansionSpec(POSType.AdvP),
    ],
    weight=0.2,
)

# VP1 -> V1
vp1__v = GrammarRule(
    SourceSpec(
        POSType.VP,
        {
            AttributeType.VALENCY: Valency.MONOVALENT,
        },
    ),
    [
        ExpansionSpec(
            POSType.Verb,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VALENCY: INHERIT,
            },
        ),
    ],
)

# VP2 -> V NP.Acc
vp2__v_npAcc = GrammarRule(
    SourceSpec(POSType.VP, {AttributeType.VALENCY: Valency.DIVALENT}),
    [
        ExpansionSpec(
            POSType.Verb,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VALENCY: INHERIT,
            },
        ),
        ExpansionSpec(
            POSType.NP,
            {
                AttributeType.NUMBER: INHERIT,
                AttributeType.CASE: Case.OBJECTIVE,
            },
        ),
    ],
)


# VP -> VP PP
vp__vp_pp = GrammarRule(
    SourceSpec(POSType.VP),
    [
        ExpansionSpec(
            POSType.VP,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VALENCY: INHERIT,
            },
        ),
        ExpansionSpec(POSType.PP),
    ],
    weight=0.2,
)

# VP -> VP Conj VP
vp__vp_conj_vp = GrammarRule(
    SourceSpec(POSType.VP),
    [
        ExpansionSpec(
            POSType.VP,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VALENCY: INHERIT,
            },
        ),
        ExpansionSpec(POSType.CoordConj),
        ExpansionSpec(
            POSType.VP,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
    ],
    weight=0.2,
)


vp_expansions = [
    vp__vp_advp,
    vp__vp_pp,
    vp__vp_conj_vp,
    vp1__v,
    vp2__v_npAcc,
]
