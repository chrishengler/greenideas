from greenideas.rules.default_english_rules.attributes.case import Case
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.npform import NPForm
from greenideas.rules.default_english_rules.attributes.person import Person
from greenideas.rules.default_english_rules.attributes.valency import Valency
from greenideas.rules.default_english_rules.attributes.voice import Voice
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# VP -> VP AdvP
vp__vp_advp = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.VP,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: INHERIT,
            },
        ),
        ExpansionSpec(DefaultEnglishPOSType.AdvP),
    ],
    weight=0.2,
)

# VP1 -> V1
vp1__v = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP,
        {
            DefaultEnglishAttributeType.VALENCY: Valency.MONOVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: INHERIT,
            },
        ),
    ],
)

# VP2 -> V NP.Obj
vp2__v_npAcc = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP,
        {
            DefaultEnglishAttributeType.VALENCY: Valency.DIVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: INHERIT,
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

# VP3 -> V NP.Obj NP.Obj
vp3__v_npAcc_npNom = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP,
        {
            DefaultEnglishAttributeType.VALENCY: Valency.TRIVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.NPFORM: NPForm.PRONOMINAL,
                DefaultEnglishAttributeType.CASE: Case.OBJECTIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.NPFORM: NPForm.LEXICAL,
                DefaultEnglishAttributeType.CASE: Case.OBJECTIVE,
                DefaultEnglishAttributeType.PERSON: Person.THIRD,
            },
        ),
    ],
)


# VP -> VP PP
vp__vp_pp = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.VP,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: INHERIT,
            },
        ),
        ExpansionSpec(DefaultEnglishPOSType.PP),
    ],
    weight=0.2,
)

# VP -> VP Conj VP
vp__vp_conj_vp = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.VP,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: INHERIT,
            },
        ),
        ExpansionSpec(DefaultEnglishPOSType.SimpleConj),
        ExpansionSpec(
            DefaultEnglishPOSType.VP,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.VOICE: INHERIT,
            },
        ),
    ],
    weight=0.2,
    ignore_after_depth=4,
)

# vp_passive -> VP_Passive
vp_pass__vpPass = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP, {DefaultEnglishAttributeType.VOICE: Voice.PASSIVE}
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.VP_Passive,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.VALENCY: [
                    Valency.DIVALENT,
                    Valency.TRIVALENT,
                ],
            },
        )
    ],
)


vp_expansions = [
    vp__vp_advp,
    vp__vp_pp,
    vp__vp_conj_vp,
    vp1__v,
    vp2__v_npAcc,
    vp3__v_npAcc_npNom,
    vp_pass__vpPass,
]
