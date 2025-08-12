from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.number import Number
from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType


class DetFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Det:
            raise TwaddleConversionError(
                f"Tried to use DetFormattingHandler on {node.type}"
            )
        name = "det"
        number = node.attributes.get(AttributeType.NUMBER)
        form = "pl" if number == Number.PLURAL else "sg"
        return f"<{name}{('.' + form if form else '')}>"
