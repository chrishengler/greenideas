from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType


class AdjFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Adj:
            raise TwaddleConversionError(
                f"Tried to use AdjFormattingHandler on {node.type}"
            )
        return "<adj>"
