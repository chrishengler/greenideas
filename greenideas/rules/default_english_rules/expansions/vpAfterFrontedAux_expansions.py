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

vpAfterFA__vpAfterFA_pp = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_AfterFrontedAux),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA__vpAfterFA_advp = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_AfterFrontedAux),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA__advP_vpAfterFA = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_AfterFrontedAux),
    [
        ExpansionSpec(DefaultEnglishPOSType.AdvP),
        ExpansionSpec(
            DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA1_simple = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA1_pa = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA1_proga = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA1_ppa = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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


vpAfterFA1_pp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)

vpAfterFA1_progp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)

vpAfterFA1_ppp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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
                DefaultEnglishAttributeType.VALENCY: INHERIT,
                DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
            },
        ),
    ],
)

vpAfterFA2_simple = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA2_pa = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA2_proga = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA2_ppa = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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
vpAfterFA2_pp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA2_progp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA2_ppp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA3_simple = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA3_pa = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA3_proga = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA3_ppa = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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


vpAfterFA3_pp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA3_progp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA3_ppp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.VP_AfterFrontedAux,
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

vpAfterFA_expansions = [
    vpAfterFA__vpAfterFA_advp,
    vpAfterFA__advP_vpAfterFA,
    vpAfterFA__vpAfterFA_pp,
    vpAfterFA1_simple,
    vpAfterFA1_pa,
    vpAfterFA1_proga,
    vpAfterFA1_ppa,
    vpAfterFA1_pp,
    vpAfterFA1_progp,
    vpAfterFA1_ppp,
    vpAfterFA2_simple,
    vpAfterFA2_pa,
    vpAfterFA2_proga,
    vpAfterFA2_ppa,
    vpAfterFA2_pp,
    vpAfterFA2_progp,
    vpAfterFA2_ppp,
    vpAfterFA3_simple,
    vpAfterFA3_pa,
    vpAfterFA3_proga,
    vpAfterFA3_ppa,
    vpAfterFA3_pp,
    vpAfterFA3_progp,
    vpAfterFA3_ppp,
]
