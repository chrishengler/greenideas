from greenideas.attributes.aspect import Aspect
from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# VP -> Aux_finite VP.participle
# placeholder, need to add additional attributes before implementing this correctly
auxp__auxFinite_vpParticiple = GrammarRule(
    SourceSpec(
        POSType.AuxP,
        {
            AttributeType.ASPECT: [
                Aspect.PERFECT,
            ]
        },
    ),
    [
        ExpansionSpec(
            POSType.Aux_finite,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
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
)

auxPerfprog__auxFinite_vpParticiple = GrammarRule(
    SourceSpec(
        POSType.AuxP,
        {
            AttributeType.ASPECT: Aspect.PERFECT_PROGRESSIVE,
        },
    ),
    [
        ExpansionSpec(
            POSType.Aux_finite,
            {
                AttributeType.ASPECT: Aspect.PERFECT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            POSType.Be,
            {
                AttributeType.ASPECT: Aspect.PERFECT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
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
)


auxpProg__auxFinite_vpGerund = GrammarRule(
    SourceSpec(
        POSType.AuxP,
        {
            AttributeType.ASPECT: [Aspect.PROGRESSIVE],
        },
    ),
    [
        ExpansionSpec(
            POSType.Be,
            {
                AttributeType.ASPECT: Aspect.SIMPLE,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
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
)

# AuxP -> Aux_do V_Bare
auxp__auxDo_vpBare = GrammarRule(
    SourceSpec(POSType.AuxP, {AttributeType.ASPECT: Aspect.SIMPLE}),
    [
        ExpansionSpec(
            POSType.Aux_do,
            {
                AttributeType.ASPECT: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.TENSE: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(POSType.VP_Bare),
    ],
)


auxP_expansions = [
    auxp__auxFinite_vpParticiple,
    auxPerfprog__auxFinite_vpParticiple,
    auxpProg__auxFinite_vpGerund,
    auxp__auxDo_vpBare,
]
