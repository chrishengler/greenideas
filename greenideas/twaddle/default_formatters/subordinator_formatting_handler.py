from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class SubordinatorFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Subordinator:
            raise TwaddleConversionError(
                f"Tried to use SubordinatorFormattingHandler on {node.type}"
            )
        return build_twaddle_tag("conj", class_specifier="subordinator")
