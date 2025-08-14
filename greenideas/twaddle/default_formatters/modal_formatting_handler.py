from greenideas.attributes.aspect import Aspect
from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.tense import Tense
from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class ModalFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Modal:
            raise TwaddleConversionError(
                f"Tried to use ModalFormattingHandler on {node.type}"
            )
        name = "modal"
        tense = node.attributes.get(AttributeType.TENSE)
        aspect = node.attributes.get(AttributeType.ASPECT)
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
