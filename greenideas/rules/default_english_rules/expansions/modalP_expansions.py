from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# ModalP -> Modal V_AfterModal
modalP__modal_vAfterModal = GrammarRule(
    SourceSpec(DefaultEnglishPOSType.ModalP),
    [
        ExpansionSpec(
            DefaultEnglishPOSType.Modal,
            {
                DefaultEnglishAttributeType.TENSE: INHERIT,
                DefaultEnglishAttributeType.ASPECT: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP_AfterModal,
            {
                DefaultEnglishAttributeType.ASPECT: INHERIT,
            },
        ),
    ],
)

modalP_expansions = [modalP__modal_vAfterModal]
