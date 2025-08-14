from greenideas.attributes.animacy import Animacy
from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class RelativePronounFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.RelativePron:
            raise ValueError(
                f"Tried to use RelativePronounFormattingHandler on {node.type}"
            )
        name = "rel"
        animacy = node.attributes.get(AttributeType.ANIMACY)
        match animacy:
            case Animacy.ANIMATE:
                class_specifier = "animate"
            case Animacy.INANIMATE:
                class_specifier = "inanimate"
        return build_twaddle_tag(name, class_specifier=class_specifier)
