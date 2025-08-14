from greenideas.attributes.aspect import Aspect
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.number import Number
from greenideas.attributes.person import Person
from greenideas.attributes.tense import Tense
from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class BeFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Be:
            raise TwaddleConversionError(
                f"Tried to use BeFormattingHandler on {node.type}"
            )
        name = "be"
        form = None
        aspect = node.attributes.get(AttributeType.ASPECT)
        number = node.attributes.get(AttributeType.NUMBER)
        person = node.attributes.get(AttributeType.PERSON)
        tense = node.attributes.get(AttributeType.TENSE)
        if aspect == Aspect.PROGRESSIVE:
            form = "gerund"
        elif aspect == Aspect.PERFECT:
            form = "pastpart"
        else:
            if number == Number.SINGULAR:
                if person == Person.FIRST:
                    form = "1sg"
                elif person == Person.THIRD:
                    form = "3sg"
                else:
                    form = "other"
            else:
                form = "other"
            if tense == Tense.PRESENT:
                form += "pres"
            else:
                form += "past"
        return build_twaddle_tag(name, form=form)
