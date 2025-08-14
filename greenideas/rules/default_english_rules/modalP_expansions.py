from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec

# ModalP -> Modal V_AfterModal
modalP__modal_vAfterModal = GrammarRule(
    SourceSpec(POSType.ModalP),
    [
        ExpansionSpec(
            POSType.Modal,
            {
                AttributeType.TENSE: INHERIT,
                AttributeType.ASPECT: INHERIT,
            },
        ),
        ExpansionSpec(
            POSType.VP_AfterModal,
            {
                AttributeType.ASPECT: INHERIT,
            },
        ),
    ],
)

modalP_expansions = [modalP__modal_vAfterModal]
