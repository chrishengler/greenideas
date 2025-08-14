from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.number import Number
from greenideas.attributes.person import Person
from greenideas.attributes.tense import Tense
from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class AuxFiniteFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Aux_finite:
            raise TwaddleConversionError(
                f"Tried to use AuxFiniteFormattingHandler on {node.type}"
            )
        name = "aux"
        form = None
        number = node.attributes.get(AttributeType.NUMBER)
        person = node.attributes.get(AttributeType.PERSON)
        tense = node.attributes.get(AttributeType.TENSE)
        if tense == Tense.PAST:
            form = "past"
        elif person == Person.THIRD and number == Number.SINGULAR:
            form = "s"
        return build_twaddle_tag(name, class_specifier="finite", form=form)
