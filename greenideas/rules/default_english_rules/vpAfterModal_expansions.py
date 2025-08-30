from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.attributes.npform import NPForm
from greenideas.attributes.person import Person
from greenideas.attributes.valency import Valency
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# VPAfterModal -> Adv VAfterModal
vpAfterModal__adv_vAfterModal = GrammarRule(
    SourceSpec(POSType.VP_AfterModal),
    [
        ExpansionSpec(POSType.Adv),
        ExpansionSpec(
            POSType.VP_AfterModal,
            {
                AttributeType.ASPECT: INHERIT,
            },
        ),
    ],
    weight=0.3,
)

# VPAfterModal -> VAfterModal AdvP
vpAfterModal__vAfterModal_advP = GrammarRule(
    SourceSpec(POSType.VP_AfterModal),
    [
        ExpansionSpec(
            POSType.VP_AfterModal,
            {
                AttributeType.ASPECT: INHERIT,
            },
        ),
        ExpansionSpec(POSType.AdvP),
    ],
    weight=0.2,
)

# VPAfterModal -> VAfterModal_1
vpAfterModal__vAfterModal = GrammarRule(
    SourceSpec(POSType.VP_AfterModal),
    [
        ExpansionSpec(
            POSType.Verb_AfterModal,
            {
                AttributeType.ASPECT: INHERIT,
            },
        ),
    ],
)

# VPAfterModal -> VAfterModal_1
vpAfterModal__vAfterModal = GrammarRule(
    SourceSpec(POSType.VP_AfterModal),
    [
        ExpansionSpec(
            POSType.Verb_AfterModal,
            {AttributeType.ASPECT: INHERIT, AttributeType.VALENCY: Valency.MONOVALENT},
        ),
    ],
)

# VPAfterModal -> VAfterModal_2
vpAfterModal__vAfterModal2 = GrammarRule(
    SourceSpec(POSType.VP_AfterModal),
    [
        ExpansionSpec(
            POSType.Verb_AfterModal,
            {AttributeType.ASPECT: INHERIT, AttributeType.VALENCY: Valency.DIVALENT},
        ),
        ExpansionSpec(
            POSType.NP,
            {
                AttributeType.CASE: Case.OBJECTIVE,
            },
        ),
    ],
)

# VPAfterModal -> VAfterModal_3 NP.Obj NP.Obj
vpAfterModal__vAfterModal3 = GrammarRule(
    SourceSpec(POSType.VP_AfterModal),
    [
        ExpansionSpec(
            POSType.Verb_AfterModal,
            {AttributeType.ASPECT: INHERIT, AttributeType.VALENCY: Valency.TRIVALENT},
        ),
        ExpansionSpec(
            POSType.NP,
            {
                AttributeType.NPFORM: NPForm.PRONOMINAL,
                AttributeType.CASE: Case.OBJECTIVE,
            },
        ),
        ExpansionSpec(
            POSType.NP,
            {
                AttributeType.NPFORM: NPForm.LEXICAL,
                AttributeType.CASE: Case.OBJECTIVE,
                AttributeType.PERSON: Person.THIRD,
            },
        ),
    ],
)


vpAfterModal_expansions = [
    vpAfterModal__adv_vAfterModal,
    vpAfterModal__vAfterModal_advP,
    vpAfterModal__vAfterModal,
    vpAfterModal__vAfterModal2,
    vpAfterModal__vAfterModal3,
]
