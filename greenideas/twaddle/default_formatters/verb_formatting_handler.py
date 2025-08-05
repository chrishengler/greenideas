from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.number import Number
from greenideas.attributes.person import Person
from greenideas.attributes.tense import Tense
from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType


class VerbFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Verb:
            raise TwaddleConversionError(
                f"Tried to use VerbFormattingHandler on {node.type}"
            )
        name = "verb"
        number = node.attributes.get(AttributeType.NUMBER)
        person = node.attributes.get(AttributeType.PERSON)
        tense = node.attributes.get(AttributeType.TENSE)
        form = ""
        match person:
            case Person.FIRST:
                form = "1"
            case Person.SECOND:
                form = "2"
            case Person.THIRD:
                form = "3"
            case _:
                raise TwaddleConversionError(
                    f"Invalid person attribute for verb: {person}"
                )
        form += "pl" if number == Number.PLURAL else "sg"
        form += "pres" if tense == Tense.PRESENT else "past"
        return f"<{name}{('.' + form if form else '')}>"
