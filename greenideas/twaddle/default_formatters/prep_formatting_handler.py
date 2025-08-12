from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType


class PrepFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Prep:
            raise TwaddleConversionError(
                f"Tried to use PrepFormattingHandler on {node.type}"
            )
        return "<prep>"
