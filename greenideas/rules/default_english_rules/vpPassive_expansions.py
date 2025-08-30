from greenideas.attributes.aspect import Aspect
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.voice import Voice
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# VP_passive
vp__passive_simple = GrammarRule(
    SourceSpec(
        POSType.VP_Passive,
        {
            AttributeType.ASPECT: Aspect.SIMPLE,
        },
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

# VP_passive_prog
vp__passive_prog = GrammarRule(
    SourceSpec(
        POSType.VP_Passive,
        {
            AttributeType.ASPECT: [Aspect.PROGRESSIVE, Aspect.PERFECT_PROGRESSIVE],
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

vp__passive_perf = GrammarRule(
    SourceSpec(
        POSType.VP_Passive,
        {
            AttributeType.ASPECT: Aspect.PERFECT,
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


vp_passive_expansions = [
    vp__passive_simple,
    vp__passive_perf,
    vp__passive_prog,
]
