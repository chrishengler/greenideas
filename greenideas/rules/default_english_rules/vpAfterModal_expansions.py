from greenideas.attributes.attribute_type import AttributeType
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
            POSType.Verb_AfterModal,
            {
                AttributeType.ASPECT: INHERIT,
            },
        ),
    ],
)

# VPAfterModal -> VAfterModal
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

# VPAfterModal -> VAfterModal AdvP
vpAfterModal__vAfterModal_advP = GrammarRule(
    SourceSpec(POSType.VP_AfterModal),
    [
        ExpansionSpec(
            POSType.Verb_AfterModal,
            {
                AttributeType.ASPECT: INHERIT,
            },
        ),
        ExpansionSpec(POSType.AdvP),
    ],
)

vpAfterModal_expansions = [
    vpAfterModal__adv_vAfterModal,
    vpAfterModal__vAfterModal,
    vpAfterModal__vAfterModal_advP,
]
