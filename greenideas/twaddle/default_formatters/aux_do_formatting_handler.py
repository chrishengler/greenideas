from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.number import Number
from greenideas.rules.default_english_rules.attributes.person import Person
from greenideas.rules.default_english_rules.attributes.tense import Tense
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class AuxDoFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != DefaultEnglishPOSType.Aux_do:
            raise TwaddleConversionError(
                f"Tried to use AuxDoFormattingHandler on {node.type}"
            )
        name = "aux"
        form = None
        number = node.attributes.get(DefaultEnglishAttributeType.NUMBER)
        person = node.attributes.get(DefaultEnglishAttributeType.PERSON)
        tense = node.attributes.get(DefaultEnglishAttributeType.TENSE)
        if tense == Tense.PAST:
            form = "past"
        elif person == Person.THIRD and number == Number.SINGULAR:
            form = "s"
        return build_twaddle_tag(name, class_specifier="do", form=form)
