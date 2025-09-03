from greenideas.attributes.aspect import Aspect
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.attributes.valency import Valency
from greenideas.attributes.voice import Voice
from greenideas.parts_of_speech.default_english_pos_types import DefaultEnglishPOSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# VP2_passive
vp2__passive_simple = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_Passive,
        {AttributeType.ASPECT: Aspect.SIMPLE, AttributeType.VALENCY: Valency.DIVALENT},
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
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
        DefaultEnglishPOSType.VP_Passive,
        {
            AttributeType.ASPECT: [Aspect.PROGRESSIVE, Aspect.PERFECT_PROGRESSIVE],
            AttributeType.VALENCY: Valency.DIVALENT,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                AttributeType.TENSE: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                AttributeType.ASPECT: Aspect.PROGRESSIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
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
        DefaultEnglishPOSType.VP_Passive,
        {
            AttributeType.ASPECT: Aspect.PERFECT,
            AttributeType.VALENCY: Valency.DIVALENT,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Aux_finite,
            {
                AttributeType.TENSE: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                AttributeType.ASPECT: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
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
        DefaultEnglishPOSType.VP_Passive,
        {AttributeType.ASPECT: Aspect.SIMPLE, AttributeType.VALENCY: Valency.TRIVALENT},
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: Voice.PASSIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                AttributeType.CASE: Case.OBJECTIVE,
            },
        ),
    ],
)

# VP_passive_prog w/ NP.obj
vp3__passive_prog = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_Passive,
        {
            AttributeType.ASPECT: [Aspect.PROGRESSIVE, Aspect.PERFECT_PROGRESSIVE],
            AttributeType.VALENCY: Valency.TRIVALENT,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                AttributeType.TENSE: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                AttributeType.ASPECT: Aspect.PROGRESSIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: Voice.PASSIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                AttributeType.CASE: Case.OBJECTIVE,
            },
        ),
    ],
)

#
vp3__passive_perf = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_Passive,
        {
            AttributeType.ASPECT: Aspect.PERFECT,
            AttributeType.VALENCY: Valency.TRIVALENT,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Aux_finite,
            {
                AttributeType.TENSE: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                AttributeType.ASPECT: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                AttributeType.VALENCY: INHERIT,
                AttributeType.VOICE: Voice.PASSIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
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
