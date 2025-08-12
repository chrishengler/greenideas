# NP -> Det NP_NoDet
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.person import Person
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

np__det_npNodet = GrammarRule(
    SourceSpec(
        POSType.NP,
        {AttributeType.PERSON: Person.THIRD},
    ),
    [
        ExpansionSpec(
            POSType.Det,
            {AttributeType.NUMBER: INHERIT, AttributeType.CASE: INHERIT},
        ),
        ExpansionSpec(
            POSType.NP_NoDet,
            {AttributeType.NUMBER: INHERIT, AttributeType.CASE: INHERIT},
        ),
    ],
)

# NP -> Pron
np__pron = GrammarRule(
    SourceSpec(POSType.NP),
    [
        ExpansionSpec(
            POSType.Pron,
            {
                AttributeType.NUMBER: INHERIT,
                AttributeType.PERSON: INHERIT,
                AttributeType.CASE: INHERIT,
            },
        )
    ],
)

np_expansions = [
    np__det_npNodet,
    np__pron,
]
