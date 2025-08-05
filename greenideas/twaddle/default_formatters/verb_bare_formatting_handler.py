from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType


class VerbBareFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Verb_Bare:
            raise TwaddleConversionError(
                f"Tried to use VerbBareFormattingHandler on {node.type}"
            )
        return "<verb>"
