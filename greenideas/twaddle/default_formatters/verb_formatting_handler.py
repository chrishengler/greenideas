from greenideas.attributes.aspect import Aspect
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.number import Number
from greenideas.attributes.person import Person
from greenideas.attributes.tense import Tense
from greenideas.attributes.valency import Valency
from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class VerbFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Verb:
            raise TwaddleConversionError(
                f"Tried to use VerbFormattingHandler on {node.type}"
            )
        name = "verb"
        form = None
        number = node.attributes.get(AttributeType.NUMBER)
        person = node.attributes.get(AttributeType.PERSON)
        tense = node.attributes.get(AttributeType.TENSE)
        aspect = node.attributes.get(AttributeType.ASPECT)
        valency = node.attributes.get(AttributeType.VALENCY)
        match valency:
            case Valency.MONOVALENT:
                class_specifier = "monovalent"
            case Valency.DIVALENT:
                class_specifier = "divalent"
            case _:
                raise TwaddleConversionError(f"Invalid valency: {valency}")
        if aspect == Aspect.PROGRESSIVE or aspect == Aspect.PERFECT_PROGRESSIVE:
            form = "gerund"
        elif aspect == Aspect.PERFECT:
            form = "pastpart"
        elif tense == Tense.PAST:
            form = "past"
        elif person == Person.THIRD and number == Number.SINGULAR:
            form = "s"
        return build_twaddle_tag(name, class_specifier=class_specifier, form=form)
