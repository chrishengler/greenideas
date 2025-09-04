from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.attributes.animacy import Animacy
from greenideas.rules.default_english_rules.attributes.case import Case
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.number import Number
from greenideas.rules.default_english_rules.attributes.person import Person
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class PronFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != DefaultEnglishPOSType.Pron:
            raise TwaddleConversionError(
                f"Tried to use PronFormattingHandler on {node.type}"
            )
        name = "pron"
        class_specifiers = list()
        person = node.attributes.get(DefaultEnglishAttributeType.PERSON)
        animacy = node.attributes.get(DefaultEnglishAttributeType.ANIMACY)
        match person:
            case Person.FIRST:
                class_specifiers.append("firstperson")
            case Person.SECOND:
                class_specifiers.append("secondperson")
            case Person.THIRD:
                class_specifiers.append("thirdperson")
                # animacy only relevant in third person
                match animacy:
                    case Animacy.ANIMATE:
                        class_specifiers.append("animate")
                    case Animacy.INANIMATE:
                        class_specifiers.append("inanimate")
        number = node.attributes.get(DefaultEnglishAttributeType.NUMBER)
        case = node.attributes.get(DefaultEnglishAttributeType.CASE)
        form = "pl" if number == Number.PLURAL else "sg"
        if case == Case.GENITIVE:
            form += "gen"
        elif case == Case.OBJECTIVE:
            form += "obj"
        return build_twaddle_tag(name, class_specifier=class_specifiers, form=form)
