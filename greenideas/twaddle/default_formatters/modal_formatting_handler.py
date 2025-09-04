from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.attributes.aspect import Aspect
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.tense import Tense
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class ModalFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != DefaultEnglishPOSType.Modal:
            raise TwaddleConversionError(
                f"Tried to use ModalFormattingHandler on {node.type}"
            )
        name = "modal"
        tense = node.attributes.get(DefaultEnglishAttributeType.TENSE)
        aspect = node.attributes.get(DefaultEnglishAttributeType.ASPECT)

        match tense:
            case Tense.PAST:
                form = "past"
            case Tense.PRESENT:
                form = "pres"
            case _:
                raise TwaddleConversionError(
                    f"Invalid tense {tense} for ModalFormattingHandler"
                )
        match aspect:
            case Aspect.PERFECT:
                form += "perf"
            case Aspect.PROGRESSIVE:
                form += "prog"
            case Aspect.PERFECT_PROGRESSIVE:
                form += "perfprog"
            case Aspect.SIMPLE:
                pass
            case _:
                raise TwaddleConversionError(
                    f"Invalid aspect {aspect} for ModalFormattingHandler"
                )
        return build_twaddle_tag(name, form=form)
