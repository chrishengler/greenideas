from greenideas.attributes.aspect import Aspect
from greenideas.attributes.attribute_type import AttributeType
from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class VerbAfterModalFormattingHandler:
    @staticmethod
    def format(node: POSNode) -> str:
        if node.type != POSType.Verb_AfterModal:
            raise TwaddleConversionError(
                f"Tried to use VerbAfterModalFormattingHandler on {node.type}"
            )
        # TODO: handle form selection based on aspect
        aspect = node.attributes.get(AttributeType.ASPECT)
        form = None
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
        return build_twaddle_tag("verb", form=form)
