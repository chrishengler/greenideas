from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.attributes.person import Person
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.grammar_ruleset import GrammarRuleset
from greenideas.rules.source_spec import SourceSpec

default_rules = GrammarRuleset()

# S -> NP VP
default_rules.add(
    GrammarRule(
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
                {AttributeType.NUMBER: INHERIT, AttributeType.PERSON: INHERIT},
            ),
        ],
    )
)

# NP -> Det NP_NoDet
default_rules.add(
    GrammarRule(
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
)

default_rules.add(
    GrammarRule(
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
)

# NP_NoDet -> Adj NP_NoDet
default_rules.add(
    GrammarRule(
        SourceSpec(POSType.NP_NoDet),
        [
            ExpansionSpec(POSType.Adj),
            ExpansionSpec(
                POSType.NP_NoDet,
                {AttributeType.NUMBER: INHERIT, AttributeType.CASE: INHERIT},
            ),
        ],
        weight=0.2,
    )
)

# NP_NoDet -> Adj N
default_rules.add(
    GrammarRule(
        SourceSpec(POSType.NP_NoDet),
        [
            ExpansionSpec(POSType.Adj),
            ExpansionSpec(
                POSType.Noun,
                {AttributeType.NUMBER: INHERIT, AttributeType.CASE: INHERIT},
            ),
        ],
        weight=0.2,
    )
)

# NP_NoDet -> N
default_rules.add(
    GrammarRule(
        SourceSpec(POSType.NP_NoDet),
        [
            ExpansionSpec(
                POSType.Noun,
                {AttributeType.NUMBER: INHERIT, AttributeType.CASE: INHERIT},
            ),
        ],
    )
)

# VP -> V NP.Acc
default_rules.add(
    GrammarRule(
        SourceSpec(POSType.VP),
        [
            ExpansionSpec(
                POSType.Verb,
                {
                    AttributeType.NUMBER: INHERIT,
                    AttributeType.TENSE: INHERIT,
                    AttributeType.PERSON: INHERIT,
                },
            ),
            ExpansionSpec(
                POSType.NP,
                {
                    AttributeType.NUMBER: INHERIT,
                    AttributeType.CASE: Case.OBJECTIVE,
                },
            ),
        ],
    )
)

# VP -> Aux_do VP(bare)
default_rules.add(
    GrammarRule(
        SourceSpec(POSType.VP),
        [
            ExpansionSpec(
                POSType.Aux_do,
                {
                    AttributeType.NUMBER: INHERIT,
                    AttributeType.TENSE: INHERIT,
                    AttributeType.PERSON: INHERIT,
                },
            ),
            ExpansionSpec(POSType.VP_Bare),
        ],
    )
)

# VP_Bare -> Adv VP(bare)
default_rules.add(
    GrammarRule(
        SourceSpec(POSType.VP_Bare),
        [
            ExpansionSpec(POSType.Adv),
            ExpansionSpec(
                POSType.VP_Bare,
            ),
        ],
        weight=0.2,
    )
)

# VP_Bare -> Verb(bare)
default_rules.add(
    GrammarRule(
        SourceSpec(POSType.VP_Bare),
        [
            ExpansionSpec(
                POSType.Verb_Bare,
            )
        ],
    )
)


# VP -> Aux_finite VP.participle

# PP -> Prep NP
default_rules.add(
    GrammarRule(
        SourceSpec(POSType.PP), [ExpansionSpec(POSType.Prep), ExpansionSpec(POSType.NP)]
    )
)
