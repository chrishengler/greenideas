from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.attributes.animacy import Animacy
from greenideas.rules.default_english_rules.attributes.case import Case
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.number import Number
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class NounFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != DefaultEnglishPOSType.Noun:
            raise TwaddleConversionError(
                f"Tried to use NounFormattingHandler on {node.type}"
            )
        name = "noun"
        class_specifier = None
        animacy = node.attributes.get(DefaultEnglishAttributeType.ANIMACY)
        number = node.attributes.get(DefaultEnglishAttributeType.NUMBER)
        case = node.attributes.get(DefaultEnglishAttributeType.CASE)
        form = "pl" if number == Number.PLURAL else "sg"
        if case == Case.GENITIVE:
            form += "gen"
        match animacy:
            case Animacy.ANIMATE:
                class_specifier = "animate"
            case Animacy.INANIMATE:
                class_specifier = "inanimate"
        return build_twaddle_tag(name, class_specifier=class_specifier, form=form)
