from greenideas.attributes.aspect import Aspect
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.attributes.valency import Valency
from greenideas.attributes.voice import Voice
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# VP2_passive
vp2__passive_simple = GrammarRule(
    SourceSpec(
        POSType.VP_Passive,
        {AttributeType.ASPECT: Aspect.SIMPLE, AttributeType.VALENCY: Valency.DIVALENT},
    ),
    [
        ExpansionSpec(
            POSType.Be,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            POSType.Verb,
            {
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: Voice.PASSIVE,
            },
        ),
    ],
)

# VP2_passive_prog
vp2__passive_prog = GrammarRule(
    SourceSpec(
        POSType.VP_Passive,
        {
            AttributeType.ASPECT: [Aspect.PROGRESSIVE, Aspect.PERFECT_PROGRESSIVE],
            AttributeType.VALENCY: Valency.DIVALENT,
        },
    ),
    [
        ExpansionSpec(
            POSType.Be,
            {
                AttributeType.TENSE: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            POSType.Be,
            {
                AttributeType.ASPECT: Aspect.PROGRESSIVE,
            },
        ),
        ExpansionSpec(
            POSType.Verb,
            {
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: Voice.PASSIVE,
            },
        ),
    ],
)

# VP2 -> passperf
vp2__passive_perf = GrammarRule(
    SourceSpec(
        POSType.VP_Passive,
        {
            AttributeType.ASPECT: Aspect.PERFECT,
            AttributeType.VALENCY: Valency.DIVALENT,
        },
    ),
    [
        ExpansionSpec(
            POSType.Aux_finite,
            {
                AttributeType.TENSE: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            POSType.Be,
            {
                AttributeType.ASPECT: INHERIT,
            },
        ),
        ExpansionSpec(
            POSType.Verb,
            {
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: Voice.PASSIVE,
            },
        ),
    ],
)

# VP3_passive w/ NP.obj
vp3__passive_simple = GrammarRule(
    SourceSpec(
        POSType.VP_Passive,
        {AttributeType.ASPECT: Aspect.SIMPLE, AttributeType.VALENCY: Valency.TRIVALENT},
    ),
    [
        ExpansionSpec(
            POSType.Be,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            POSType.Verb,
            {
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: Voice.PASSIVE,
            },
        ),
        ExpansionSpec(
            POSType.NP,
            {
                AttributeType.CASE: Case.OBJECTIVE,
            },
        ),
    ],
)

# VP_passive_prog w/ NP.obj
vp3__passive_prog = GrammarRule(
    SourceSpec(
        POSType.VP_Passive,
        {
            AttributeType.ASPECT: [Aspect.PROGRESSIVE, Aspect.PERFECT_PROGRESSIVE],
            AttributeType.VALENCY: Valency.TRIVALENT,
        },
    ),
    [
        ExpansionSpec(
            POSType.Be,
            {
                AttributeType.TENSE: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            POSType.Be,
            {
                AttributeType.ASPECT: Aspect.PROGRESSIVE,
            },
        ),
        ExpansionSpec(
            POSType.Verb,
            {
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: Voice.PASSIVE,
            },
        ),
        ExpansionSpec(
            POSType.NP,
            {
                AttributeType.CASE: Case.OBJECTIVE,
            },
        ),
    ],
)

#
vp3__passive_perf = GrammarRule(
    SourceSpec(
        POSType.VP_Passive,
        {
            AttributeType.ASPECT: Aspect.PERFECT,
            AttributeType.VALENCY: Valency.TRIVALENT,
        },
    ),
    [
        ExpansionSpec(
            POSType.Aux_finite,
            {
                AttributeType.TENSE: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            POSType.Be,
            {
                AttributeType.ASPECT: INHERIT,
            },
        ),
        ExpansionSpec(
            POSType.Verb,
            {
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: Voice.PASSIVE,
            },
        ),
        ExpansionSpec(
            POSType.NP,
            {
                AttributeType.CASE: Case.OBJECTIVE,
            },
        ),
    ],
)
vp_passive_expansions = [
    vp2__passive_simple,
    vp2__passive_perf,
    vp2__passive_prog,
    vp3__passive_simple,
    vp3__passive_perf,
    vp3__passive_prog,
]
