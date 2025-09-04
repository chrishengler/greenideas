from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class CoordconjFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != DefaultEnglishPOSType.CoordConj:
            raise TwaddleConversionError(
                f"Tried to use CoordconjFormattingHandler on {node.type}"
            )
        return build_twaddle_tag("conj", class_specifier="coordinating")
