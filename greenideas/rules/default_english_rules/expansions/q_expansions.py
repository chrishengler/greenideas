from greenideas.rules.default_english_rules.attributes.aspect import Aspect
from greenideas.rules.default_english_rules.attributes.case import Case
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.npform import NPForm
from greenideas.rules.default_english_rules.attributes.person import Person
from greenideas.rules.default_english_rules.attributes.tense import Tense
from greenideas.rules.default_english_rules.attributes.voice import Voice
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

q__auxDo_np_vp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.Q,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Aux_do,
            {
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.CASE: Case.NOMINATIVE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP_Bare,
        ),
    ],
)

q__auxFinite_np_vp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.Q,
        {
            DefaultEnglishAttributeType.ASPECT: [
                Aspect.PERFECT,
                Aspect.PERFECT_PROGRESSIVE,
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
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.CASE: Case.NOMINATIVE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP_AfterFrontedAux,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
            },
        ),
    ],
)

qProg__be_np_vp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.Q,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.PROGRESSIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.CASE: Case.NOMINATIVE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP_AfterFrontedAux,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
            },
        ),
    ],
)

qSimplePast__be_np_vpAfterAF = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.Q,
        {
            DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
            DefaultEnglishAttributeType.TENSE: Tense.PAST,
            DefaultEnglishAttributeType.VOICE: Voice.PASSIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.CASE: Case.NOMINATIVE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP_AfterFrontedAux,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
            },
        ),
    ],
)

q__be_np_adjp = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.Q),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.CASE: Case.NOMINATIVE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(DefaultEnglishPOSType.AdjP),
    ],
)

q__be_np_np = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.Q),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.CASE: Case.NOMINATIVE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.CASE: Case.NOMINATIVE,
                DefaultEnglishAttributeType.NPFORM: NPForm.LEXICAL,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: Person.THIRD,
            },
        ),
    ],
)

question_expansions = [
    q__auxDo_np_vp,
    q__auxFinite_np_vp,
    qProg__be_np_vp,
    qSimplePast__be_np_vpAfterAF,
    q__be_np_adjp,
    q__be_np_np,
]
