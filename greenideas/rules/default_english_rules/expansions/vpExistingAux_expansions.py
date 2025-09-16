# Residual VP after fronted finite auxiliary
from greenideas.rules.default_english_rules.attributes.aspect import Aspect
from greenideas.rules.default_english_rules.attributes.case import Case
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.npform import NPForm
from greenideas.rules.default_english_rules.attributes.person import Person
from greenideas.rules.default_english_rules.attributes.tense import Tense
from greenideas.rules.default_english_rules.attributes.valency import Valency
from greenideas.rules.default_english_rules.attributes.voice import Voice
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

vpExistingAux__vpExistingAux_pp = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_ExistingAux),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.VP_ExistingAux,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.VOICE: INHERIT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
            },
        ),
        ExpansionSpec(DefaultEnglishPOSType.PP),
    ],
    weight=0.1,
    ignore_after_depth=3,
)

vpExistingAux__vpExistingAux_advp = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_ExistingAux),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.VP_ExistingAux,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.VOICE: INHERIT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
            },
        ),
        ExpansionSpec(DefaultEnglishPOSType.AdvP),
    ],
    weight=0.1,
    ignore_after_depth=3,
)

vpExistingAux__advP_vpExistingAux = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_ExistingAux),
    [
        ExpansionSpec(DefaultEnglishPOSType.AdvP),
        ExpansionSpec(
            DefaultEnglishPOSType.VP_ExistingAux,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.VOICE: INHERIT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
            },
        ),
    ],
    weight=0.1,
    ignore_after_depth=3,
)

vpExistingAux1_simple = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
            DefaultEnglishAttributeType.VALENCY: Valency.MONOVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
                DefaultEnglishAttributeType.TENSE: Tense.PRESENT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)

vpExistingAux1_pa = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
            DefaultEnglishAttributeType.VALENCY: Valency.MONOVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
                DefaultEnglishAttributeType.TENSE: Tense.PAST,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)

vpExistingAux1_proga = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
            DefaultEnglishAttributeType.VALENCY: Valency.MONOVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)

vpExistingAux1_ppa = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT_PROGRESSIVE,
            DefaultEnglishAttributeType.VALENCY: Valency.MONOVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT},
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)


vpExistingAux1_pp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
            DefaultEnglishAttributeType.VALENCY: Valency.MONOVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
                DefaultEnglishAttributeType.TENSE: Tense.PAST,
                DefaultEnglishAttributeType.VALENCY: [
                    Valency.DIVALENT,
                    Valency.TRIVALENT,
                ],
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)

vpExistingAux1_progp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
            DefaultEnglishAttributeType.VALENCY: Valency.MONOVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
                DefaultEnglishAttributeType.VALENCY: [
                    Valency.DIVALENT,
                    Valency.TRIVALENT,
                ],
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)

vpExistingAux1_ppp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT_PROGRESSIVE,
            DefaultEnglishAttributeType.VALENCY: Valency.MONOVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT},
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
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
                DefaultEnglishAttributeType.VALENCY: [
                    Valency.DIVALENT,
                    Valency.TRIVALENT,
                ],
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)

vpExistingAux2_simple = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
            DefaultEnglishAttributeType.VALENCY: Valency.DIVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
                DefaultEnglishAttributeType.TENSE: Tense.PRESENT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
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

vpExistingAux2_pa = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
            DefaultEnglishAttributeType.VALENCY: Valency.DIVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
                DefaultEnglishAttributeType.TENSE: Tense.PAST,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
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

vpExistingAux2_proga = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
            DefaultEnglishAttributeType.VALENCY: Valency.DIVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
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

vpExistingAux2_ppa = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT_PROGRESSIVE,
            DefaultEnglishAttributeType.VALENCY: Valency.DIVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT},
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)


# passive monovalents -> convert to divalent
vpExistingAux2_pp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
            DefaultEnglishAttributeType.VALENCY: [Valency.MONOVALENT, Valency.DIVALENT],
            DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
                DefaultEnglishAttributeType.TENSE: Tense.PAST,
                DefaultEnglishAttributeType.VALENCY: Valency.DIVALENT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)

vpExistingAux2_progp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
            DefaultEnglishAttributeType.VALENCY: [Valency.MONOVALENT, Valency.DIVALENT],
            DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
                DefaultEnglishAttributeType.VALENCY: Valency.DIVALENT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)

vpExistingAux2_ppp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.VALENCY: [Valency.MONOVALENT, Valency.DIVALENT],
            DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT},
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
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
                DefaultEnglishAttributeType.VALENCY: Valency.DIVALENT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)

vpExistingAux3_simple = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
            DefaultEnglishAttributeType.VALENCY: Valency.TRIVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
                DefaultEnglishAttributeType.TENSE: Tense.PRESENT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
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

vpExistingAux3_pa = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
            DefaultEnglishAttributeType.VALENCY: Valency.TRIVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
                DefaultEnglishAttributeType.TENSE: Tense.PAST,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
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

vpExistingAux3_proga = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
            DefaultEnglishAttributeType.VALENCY: Valency.TRIVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
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

vpExistingAux3_ppa = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT_PROGRESSIVE,
            DefaultEnglishAttributeType.VALENCY: Valency.TRIVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT},
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
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


vpExistingAux3_pp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
            DefaultEnglishAttributeType.VALENCY: Valency.TRIVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
                DefaultEnglishAttributeType.TENSE: Tense.PAST,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
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

vpExistingAux3_progp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
            DefaultEnglishAttributeType.VALENCY: Valency.TRIVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Verb,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
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

vpExistingAux3_ppp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_ExistingAux,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT_PROGRESSIVE,
            DefaultEnglishAttributeType.VALENCY: Valency.TRIVALENT,
            DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT},
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
                DefaultEnglishAttributeType.ASPECT: Aspect.PERFECT,
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
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

vpExistingAux_expansions = [
    vpExistingAux__vpExistingAux_advp,
    vpExistingAux__advP_vpExistingAux,
    vpExistingAux__vpExistingAux_pp,
    vpExistingAux1_simple,
    vpExistingAux1_pa,
    vpExistingAux1_proga,
    vpExistingAux1_ppa,
    vpExistingAux1_pp,
    vpExistingAux1_progp,
    vpExistingAux1_ppp,
    vpExistingAux2_simple,
    vpExistingAux2_pa,
    vpExistingAux2_proga,
    vpExistingAux2_ppa,
    vpExistingAux2_pp,
    vpExistingAux2_progp,
    vpExistingAux2_ppp,
    vpExistingAux3_simple,
    vpExistingAux3_pa,
    vpExistingAux3_proga,
    vpExistingAux3_ppa,
    vpExistingAux3_pp,
    vpExistingAux3_progp,
    vpExistingAux3_ppp,
]
