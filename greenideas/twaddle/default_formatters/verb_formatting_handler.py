from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.attributes.aspect import Aspect
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.number import Number
from greenideas.rules.default_english_rules.attributes.person import Person
from greenideas.rules.default_english_rules.attributes.tense import Tense
from greenideas.rules.default_english_rules.attributes.valency import Valency
from greenideas.rules.default_english_rules.attributes.voice import Voice
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class VerbFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != DefaultEnglishPOSType.Verb:
            raise TwaddleConversionError(
                f"Tried to use VerbFormattingHandler on {node.type}"
            )
        name = "verb"
        form = None
        number = node.attributes.get(DefaultEnglishAttributeType.NUMBER)
        person = node.attributes.get(DefaultEnglishAttributeType.PERSON)
        tense = node.attributes.get(DefaultEnglishAttributeType.TENSE)
        aspect = node.attributes.get(DefaultEnglishAttributeType.ASPECT)
        valency = node.attributes.get(DefaultEnglishAttributeType.VALENCY)
        voice = node.attributes.get(DefaultEnglishAttributeType.VOICE)

        match valency:
            case Valency.MONOVALENT:
                class_specifier = "monovalent"
            case Valency.DIVALENT:
                class_specifier = "divalent"
            case Valency.TRIVALENT:
                class_specifier = "trivalent"
            case _:
                raise TwaddleConversionError(f"Invalid valency: {valency}")
        if voice == Voice.PASSIVE:
            form = "pastpart"
        elif aspect == Aspect.PROGRESSIVE or aspect == Aspect.PERFECT_PROGRESSIVE:
            form = "gerund"
        elif aspect == Aspect.PERFECT:
            form = "pastpart"
        elif tense == Tense.PAST:
            form = "past"
        elif person == Person.THIRD and number == Number.SINGULAR:
            form = "s"
        return build_twaddle_tag(name, class_specifier=class_specifier, form=form)
