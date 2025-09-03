# S -> NP VP
from greenideas.attributes.aspect import Aspect
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.attributes.npform import NPForm
from greenideas.attributes.person import Person
from greenideas.attributes.voice import Voice
from greenideas.parts_of_speech.default_english_pos_types import DefaultEnglishPOSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

s__np_vp = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.S),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                AttributeType.ANIMACY: INHERIT,
                AttributeType.CASE: Case.NOMINATIVE,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP,
            {
                AttributeType.ANIMACY: INHERIT,
                AttributeType.ASPECT: Aspect.SIMPLE,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.VOICE: INHERIT,
            },
        ),
    ],
)

# S -> NP AuxP
s__np_auxp = GrammarRule(
    SourceSpec(
        DefaultEnglishPOSType.S,
        {
            AttributeType.VOICE: Voice.ACTIVE,
        },
    ),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                AttributeType.ANIMACY: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.CASE: Case.NOMINATIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.AuxP,
            {
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.TENSE: INHERIT,
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
                AttributeType.ANIMACY: INHERIT,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.CASE: Case.NOMINATIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.ModalP,
            {
                AttributeType.TENSE: INHERIT,
            },
        ),
    ],
)

# S -> S Conj S
s__s_conj_s = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.S),
    [
        ExpansionSpec(DefaultEnglishPOSType.S),
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
                AttributeType.CASE: Case.NOMINATIVE,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                AttributeType.ASPECT: Aspect.SIMPLE,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.TENSE: INHERIT,
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
                AttributeType.CASE: Case.NOMINATIVE,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                AttributeType.ASPECT: Aspect.SIMPLE,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.TENSE: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                AttributeType.CASE: Case.NOMINATIVE,
                AttributeType.NPFORM: NPForm.LEXICAL,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: Person.THIRD,
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
                AttributeType.CASE: Case.NOMINATIVE,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.Be,
            {
                AttributeType.ASPECT: Aspect.SIMPLE,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.TENSE: INHERIT,
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
