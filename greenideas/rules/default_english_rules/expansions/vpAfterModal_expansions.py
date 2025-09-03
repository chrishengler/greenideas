from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.attributes.npform import NPForm
from greenideas.attributes.person import Person
from greenideas.attributes.valency import Valency
from greenideas.parts_of_speech.default_english_pos_types import DefaultEnglishPOSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# VPAfterModal -> Adv VAfterModal
vpAfterModal__adv_vAfterModal = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_AfterModal),
    [
        ExpansionSpec(DefaultEnglishPOSType.Adv),
        ExpansionSpec(
            DefaultEnglishPOSType.VP_AfterModal,
            {
                AttributeType.ASPECT: INHERIT,
            },
        ),
    ],
    weight=0.3,
)

# VPAfterModal -> VAfterModal AdvP
vpAfterModal__vAfterModal_advP = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_AfterModal),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.VP_AfterModal,
            {
                AttributeType.ASPECT: INHERIT,
            },
        ),
        ExpansionSpec(DefaultEnglishPOSType.AdvP),
    ],
    weight=0.2,
)

# VPAfterModal -> VAfterModal_1
vpAfterModal__vAfterModal = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_AfterModal),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb_AfterModal,
            {
                AttributeType.ASPECT: INHERIT,
            },
        ),
    ],
)

# VPAfterModal -> VAfterModal_1
vpAfterModal__vAfterModal = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_AfterModal),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb_AfterModal,
            {AttributeType.ASPECT: INHERIT, AttributeType.VALENCY: Valency.MONOVALENT},
        ),
    ],
)

# VPAfterModal -> VAfterModal_2
vpAfterModal__vAfterModal2 = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_AfterModal),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb_AfterModal,
            {AttributeType.ASPECT: INHERIT, AttributeType.VALENCY: Valency.DIVALENT},
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                AttributeType.CASE: Case.OBJECTIVE,
            },
        ),
    ],
)

# VPAfterModal -> VAfterModal_3 NP.Obj NP.Obj
vpAfterModal__vAfterModal3 = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_AfterModal),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb_AfterModal,
            {AttributeType.ASPECT: INHERIT, AttributeType.VALENCY: Valency.TRIVALENT},
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
            {
                AttributeType.NPFORM: NPForm.PRONOMINAL,
                AttributeType.CASE: Case.OBJECTIVE,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.NP,
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
