from greenideas.attributes.aspect import Aspect
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.voice import Voice
from greenideas.parts_of_speech.default_english_pos_types import DefaultEnglishPOSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# VP -> Aux_finite VP.participle
# placeholder, need to add additional attributes before implementing this correctly
auxp__auxFinite_vpParticiple = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.AuxP,
        {
            AttributeType.ASPECT: [
                Aspect.PERFECT,
            ]
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Aux_finite,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
    ],
)

auxPerfprog__auxFinite_vpParticiple = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.AuxP,
        {
            AttributeType.ASPECT: Aspect.PERFECT_PROGRESSIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Aux_finite,
            {
                AttributeType.ASPECT: Aspect.PERFECT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                AttributeType.ASPECT: Aspect.PERFECT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)


auxpProg__auxFinite_vpGerund = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.AuxP,
        {
            AttributeType.ASPECT: [Aspect.PROGRESSIVE],
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                AttributeType.ASPECT: Aspect.SIMPLE,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)

# AuxP -> Aux_do V_Bare
auxp__auxDo_vpBare = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.AuxP, {AttributeType.ASPECT: Aspect.SIMPLE}),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Aux_do,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(DefaultEnglishPOSType.VP_Bare),
    ],
)


auxP_expansions = [
    auxp__auxFinite_vpParticiple,
    auxPerfprog__auxFinite_vpParticiple,
    auxpProg__auxFinite_vpGerund,
    auxp__auxDo_vpBare,
]
