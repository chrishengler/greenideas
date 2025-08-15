from greenideas.attributes.animacy import Animacy
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.attributes.number import Number
from greenideas.attributes.person import Person
from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class PronFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Pron:
            raise TwaddleConversionError(
                f"Tried to use PronFormattingHandler on {node.type}"
            )
        name = "pron"
        class_specifiers = list()
        person = node.attributes.get(AttributeType.PERSON)
        animacy = node.attributes.get(AttributeType.ANIMACY)
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
        number = node.attributes.get(AttributeType.NUMBER)
        case = node.attributes.get(AttributeType.CASE)
        form = "pl" if number == Number.PLURAL else "sg"
        if case == Case.GENITIVE:
            form += "gen"
        elif case == Case.OBJECTIVE:
            form += "obj"
        return build_twaddle_tag(name, class_specifier=class_specifiers, form=form)
