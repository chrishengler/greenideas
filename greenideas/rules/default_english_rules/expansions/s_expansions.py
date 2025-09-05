# S -> NP VP
from greenideas.rules.default_english_rules.attributes.aspect import Aspect
from greenideas.rules.default_english_rules.attributes.case import Case
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.npform import NPForm
from greenideas.rules.default_english_rules.attributes.person import Person
from greenideas.rules.default_english_rules.attributes.voice import Voice
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

s__np_vp = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.S),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.ANIMACY: INHERIT,
                DefaultEnglishAttributeType.CASE: Case.NOMINATIVE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP,
            {
                DefaultEnglishAttributeType.ANIMACY: INHERIT,
                DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.VOICE: INHERIT,
            },
        ),
    ],
)

# S -> NP AuxP
s__np_auxp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.S,
        {
            DefaultEnglishAttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.ANIMACY: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.CASE: Case.NOMINATIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.AuxP,
            {
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
            },
        ),
    ],
)

# S -> NP ModalP
s__np_modalp = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.S),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.ANIMACY: INHERIT,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.CASE: Case.NOMINATIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.ModalP,
            {
                DefaultEnglishAttributeType.TENSE: INHERIT,
            },
        ),
    ],
)

# S -> S Conj S
s__s_conj_s = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.S),
    [
        ExpansionSpec(DefaultEnglishPOSType.S, post_punctuation=","),
        ExpansionSpec(DefaultEnglishPOSType.CoordConj),
        ExpansionSpec(DefaultEnglishPOSType.S),
    ],
    weight=0.2,
    ignore_after_depth=2,
)

s__s_sub_s = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.S),
    [
        ExpansionSpec(DefaultEnglishPOSType.S),
        ExpansionSpec(DefaultEnglishPOSType.Subordinator),
        ExpansionSpec(DefaultEnglishPOSType.S),
    ],
    weight=0.2,
    ignore_after_depth=2,
)

s__np_be_adjp = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.S),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.CASE: Case.NOMINATIVE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
            },
        ),
        ExpansionSpec(DefaultEnglishPOSType.AdjP),
    ],
)

s__np_be_np = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.S),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.CASE: Case.NOMINATIVE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
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
                DefaultEnglishAttributeType.NPFORM: NPForm.LEXICAL,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: Person.THIRD,
            },
        ),
    ],
    weight=0.3,
)

s__np_be_pp = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.S),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                DefaultEnglishAttributeType.CASE: Case.NOMINATIVE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                DefaultEnglishAttributeType.ASPECT: Aspect.SIMPLE,
                DefaultEnglishAttributeType.NUMBER: INHERIT,
                DefaultEnglishAttributeType.PERSON: INHERIT,
                DefaultEnglishAttributeType.TENSE: INHERIT,
            },
        ),
        ExpansionSpec(DefaultEnglishPOSType.PP),
    ],
)

s_expansions = [
    s__np_vp,
    s__np_auxp,
    s__np_modalp,
    s__s_conj_s,
    s__s_sub_s,
    s__np_be_adjp,
    s__np_be_np,
    s__np_be_pp,
]
