from greenideas.attributes.aspect import Aspect
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
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
            },
        ),
        ExpansionSpec(POSType.AdvP),
    ],
)

# VP -> V NP.Acc
vp__v_npAcc = GrammarRule(
    SourceSpec(POSType.VP, {AttributeType.ASPECT: Aspect.SIMPLE}),
    [
        ExpansionSpec(
            POSType.Verb,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
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

# VP.perf -> V.past
vp__v_past = GrammarRule(
    SourceSpec(POSType.VP, {AttributeType.ASPECT: Aspect.PERFECT}),
    [
        ExpansionSpec(
            POSType.Verb,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
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

# VP.prog/perfprog -> V.gerund
vp__v_gerund = GrammarRule(
    SourceSpec(
        POSType.VP,
        {AttributeType.ASPECT: [Aspect.PROGRESSIVE, Aspect.PERFECT_PROGRESSIVE]},
    ),
    [
        ExpansionSpec(
            POSType.Verb,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
    ],
)

vp_expansions = [
    vp__vp_advp,
    vp__v_npAcc,
    vp__v_past,
    vp__v_gerund,
]
