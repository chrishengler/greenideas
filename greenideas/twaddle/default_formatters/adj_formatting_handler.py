from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class AdjFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Adj:
            raise TwaddleConversionError(
                f"Tried to use AdjFormattingHandler on {node.type}"
            )
        return build_twaddle_tag(dict_name="adj")
