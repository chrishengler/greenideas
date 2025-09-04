from greenideas.rules.default_english_rules.attributes.case import Case
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.npform import NPForm
from greenideas.rules.default_english_rules.attributes.person import Person
from greenideas.rules.default_english_rules.attributes.valency import Valency
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
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
                DefaultEnglishAttributeType.ASPECT: INHERIT,
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
                DefaultEnglishAttributeType.ASPECT: INHERIT,
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
                DefaultEnglishAttributeType.ASPECT: INHERIT,
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
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.VALENCY: Valency.MONOVALENT,
            },
        ),
    ],
)

# VPAfterModal -> VAfterModal_2
vpAfterModal__vAfterModal2 = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_AfterModal),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb_AfterModal,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.VALENCY: Valency.DIVALENT,
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

# VPAfterModal -> VAfterModal_3 NP.Obj NP.Obj
vpAfterModal__vAfterModal3 = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.VP_AfterModal),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Verb_AfterModal,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
                DefaultEnglishAttributeType.VALENCY: Valency.TRIVALENT,
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


vpAfterModal_expansions = [
    vpAfterModal__adv_vAfterModal,
    vpAfterModal__vAfterModal_advP,
    vpAfterModal__vAfterModal,
    vpAfterModal__vAfterModal2,
    vpAfterModal__vAfterModal3,
]
