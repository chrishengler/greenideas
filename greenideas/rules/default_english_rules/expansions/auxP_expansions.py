from greenideas.rules.default_english_rules.attributes.aspect import Aspect
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.voice import Voice
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# VP -> Aux_finite VP.participle
# placeholder, need to add additional attributes before implementing this correctly
auxp__auxFinite_vpParticiple = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.AuxP,
        {
            DefaultEnglishAttributeType.ASPECT: [
                Aspect.PERFECT,
            ]
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Aux_finite,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
    ],
)

auxPerfprog__auxFinite_vpParticiple = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.AuxP,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT_PROGRESSIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Aux_finite,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)


auxpProg__auxFinite_vpGerund = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.AuxP,
        {
            DefaultEnglishAttributeType.ASPECT: [Aspect.PROGRESSIVE],
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)

# AuxP -> Aux_do V_Bare
auxp__auxDo_vpBare = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.AuxP, {DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE}
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Aux_do,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
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
