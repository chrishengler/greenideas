from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.attributes.number import Number
from greenideas.attributes.person import Person
from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType


class PronFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Pron:
            raise TwaddleConversionError(
                f"Tried to use PronFormattingHandler on {node.type}"
            )
        name = "pron"
        label = ""
        person = node.attributes.get(AttributeType.PERSON)
        if person == Person.FIRST:
            label = "firstperson"
        elif person == Person.SECOND:
            label = "secondperson"
        elif person == Person.THIRD:
            label = "thirdperson"
        number = node.attributes.get(AttributeType.NUMBER)
        case = node.attributes.get(AttributeType.CASE)
        form = "pl" if number == Number.PLURAL else "sg"
        if case == Case.GENITIVE:
            form += "gen"
        elif case == Case.OBJECTIVE:
            form += "obj"
        return f"<{name}-{label}{('.' + form if form else '')}>"
