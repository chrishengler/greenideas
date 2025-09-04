from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.attributes.aspect import Aspect
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


class BeFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != DefaultEnglishPOSType.Be:
            raise TwaddleConversionError(
                f"Tried to use BeFormattingHandler on {node.type}"
            )
        name = "be"
        form = None
        aspect = node.attributes.get(DefaultEnglishAttributeType.ASPECT)
        number = node.attributes.get(DefaultEnglishAttributeType.NUMBER)
        person = node.attributes.get(DefaultEnglishAttributeType.PERSON)
        tense = node.attributes.get(DefaultEnglishAttributeType.TENSE)
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
