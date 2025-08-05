from typing import Protocol

from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode


class TwaddleFormattingHandler(Protocol):
    @staticmethod
    def format(node: POSNode) -> str:
        raise TwaddleConversionError(
            "Twaddle Formatter defines a protocol and is not " "directly usable"
        )
