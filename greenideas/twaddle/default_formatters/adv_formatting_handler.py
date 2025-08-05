from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType


class AdvFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Adv:
            raise TwaddleConversionError(
                f"Tried to use AdvFormattingHandler on {node.type}"
            )
        return "<adv>"
