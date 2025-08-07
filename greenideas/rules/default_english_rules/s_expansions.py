# S -> NP VP
from greenideas.attributes.aspect import Aspect
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

s__np_vp = GrammarRule(
    SourceSpec(POSType.S),
    [
        ExpansionSpec(
            POSType.NP,
            {
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.CASE: Case.NOMINATIVE,
            },
        ),
        ExpansionSpec(
            POSType.VP,
            {
                AttributeType.ASPECT: Aspect.SIMPLE,
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
            },
        ),
    ],
)

# S -> NP AuxP
s__np_auxp = GrammarRule(
    SourceSpec(POSType.S),
    [
        ExpansionSpec(
            POSType.NP,
            {
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.CASE: Case.NOMINATIVE,
            },
        ),
        ExpansionSpec(
            POSType.AuxP,
            {
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.TENSE: INHERIT,
            },
        ),
    ],
)

# S -> S Conj S
s__s_conj_s = GrammarRule(
    SourceSpec(POSType.S),
    [
        ExpansionSpec(POSType.S),
        ExpansionSpec(POSType.Conj),
        ExpansionSpec(POSType.S),
    ],
    weight=0.05,
)

s_expansions = [
    s__np_vp,
    s__np_auxp,
    s__s_conj_s,
]
