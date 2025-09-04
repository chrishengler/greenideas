from greenideas.rules.default_english_rules.attributes.aspect import Aspect
from greenideas.rules.default_english_rules.attributes.case import Case
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.valency import Valency
from greenideas.rules.default_english_rules.attributes.voice import Voice
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# VP2_passive
vp2__passive_simple = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_Passive,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
            DefaultEnglishAttributeType.VALENCY: Valency.DIVALENT,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
            },
        ),
    ],
)

# VP2_passive_prog
vp2__passive_prog = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_Passive,
        {
            DefaultEnglishAttributeType.ASPECT: [
                Aspect.PROGRESSIVE,
                Aspect.PERFECT_PROGRESSIVE,
            ],
            DefaultEnglishAttributeType.VALENCY: Valency.DIVALENT,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
            },
        ),
    ],
)

# VP2 -> passperf
vp2__passive_perf = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_Passive,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
            DefaultEnglishAttributeType.VALENCY: Valency.DIVALENT,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Aux_finite,
            {
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
            },
        ),
    ],
)

# VP3_passive w/ NP.obj
vp3__passive_simple = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_Passive,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
            DefaultEnglishAttributeType.VALENCY: Valency.TRIVALENT,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.CASE: Case.OBJECTIVE,
            },
        ),
    ],
)

# VP_passive_prog w/ NP.obj
vp3__passive_prog = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_Passive,
        {
            DefaultEnglishAttributeType.ASPECT: [
                Aspect.PROGRESSIVE,
                Aspect.PERFECT_PROGRESSIVE,
            ],
            DefaultEnglishAttributeType.VALENCY: Valency.TRIVALENT,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.CASE: Case.OBJECTIVE,
            },
        ),
    ],
)

#
vp3__passive_perf = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_Passive,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
            DefaultEnglishAttributeType.VALENCY: Valency.TRIVALENT,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Aux_finite,
            {
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.CASE: Case.OBJECTIVE,
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
