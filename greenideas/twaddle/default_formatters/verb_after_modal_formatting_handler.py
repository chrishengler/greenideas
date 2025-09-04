from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.attributes.aspect import Aspect
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.valency import Valency
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class VerbAfterModalFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != DefaultEnglishPOSType.Verb_AfterModal:
            raise TwaddleConversionError(
                f"Tried to use VerbAfterModalFormattingHandler on {node.type}"
            )
        # TODO: handle form selection based on aspect
        aspect = node.attributes.get(DefaultEnglishAttributeType.ASPECT)
        form = None
        valency = node.attributes.get(DefaultEnglishAttributeType.VALENCY)
        match valency:
            case Valency.MONOVALENT:
                class_specifier = "monovalent"
            case Valency.DIVALENT:
                class_specifier = "divalent"
            case Valency.TRIVALENT:
                class_specifier = "trivalent"
            case _:
                raise TwaddleConversionError(f"Invalid valency: {valency}")
        match aspect:
            case Aspect.PERFECT:
                form = "pastpart"
            case Aspect.PROGRESSIVE | Aspect.PERFECT_PROGRESSIVE:
                form = "gerund"
            case Aspect.SIMPLE:
                pass
            case _:
                raise TwaddleConversionError(
                    f"Unsupported aspect {aspect} for VerbAfterModalFormattingHandler"
                )
        return build_twaddle_tag("verb", class_specifier=class_specifier, form=form)
