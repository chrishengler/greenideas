from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class SimpleConjFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.SimpleConj:
            raise TwaddleConversionError(
                f"Tried to use SimpleConjFormattingHandler on {node.type}"
            )
        return build_twaddle_tag("conj", class_specifier="simple")
