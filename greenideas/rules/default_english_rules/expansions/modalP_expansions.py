from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.default_english_pos_types import DefaultEnglishPOSType
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
                AttributeType.TENSE: INHERIT,
                AttributeType.ASPECT: INHERIT,
            },
        ),
        ExpansionSpec(
            DefaultEnglishPOSType.VP_AfterModal,
            {
                AttributeType.ASPECT: INHERIT,
            },
        ),
    ],
)

modalP_expansions = [modalP__modal_vAfterModal]
