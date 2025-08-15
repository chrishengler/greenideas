from greenideas.attributes.animacy import Animacy
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.attributes.number import Number
from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class NounFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Noun:
            raise TwaddleConversionError(
                f"Tried to use NounFormattingHandler on {node.type}"
            )
        name = "noun"
        class_specifier = None
        animacy = node.attributes.get(AttributeType.ANIMACY)
        number = node.attributes.get(AttributeType.NUMBER)
        case = node.attributes.get(AttributeType.CASE)
        form = "pl" if number == Number.PLURAL else "sg"
        if case == Case.GENITIVE:
            form += "gen"
        match animacy:
            case Animacy.ANIMATE:
                class_specifier = "animate"
            case Animacy.INANIMATE:
                class_specifier = "inanimate"
        return build_twaddle_tag(name, class_specifier=class_specifier, form=form)
