from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.valency import Valency
from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class VerbBareFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Verb_Bare:
            raise TwaddleConversionError(
                f"Tried to use VerbBareFormattingHandler on {node.type}"
            )

        valency = node.attributes.get(AttributeType.VALENCY)
        match valency:
            case Valency.MONOVALENT:
                class_specifier = "monovalent"
            case Valency.DIVALENT:
                class_specifier = "divalent"
            case _:
                raise TwaddleConversionError(f"Invalid valency: {valency}")
        return build_twaddle_tag("verb", class_specifier=class_specifier)
