from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.number import Number
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class DetFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != DefaultEnglishPOSType.Det:
            raise TwaddleConversionError(
                f"Tried to use DetFormattingHandler on {node.type}"
            )
        name = "det"
        number = node.attributes.get(DefaultEnglishAttributeType.NUMBER)
        form = "pl" if number == Number.PLURAL else "sg"
        return build_twaddle_tag(name, form=form)
