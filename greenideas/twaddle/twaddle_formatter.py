import logging
from typing import Optional

from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_type_base import POSType
from greenideas.twaddle.formatting_context import FormattingContext
from greenideas.twaddle.twaddle_formatting_handler import TwaddleFormattingHandler

logger = logging.getLogger(__file__)


class TwaddleFormatter:
    def __init__(self):
        self.formatting_handlers: dict[POSType, TwaddleFormattingHandler] = dict()

    def register_formatting_handler(
        self, pos: POSType, handler: TwaddleFormattingHandler
    ):
        self.formatting_handlers[pos] = handler

    def format_node(
        self, node: POSNode, context: Optional[FormattingContext] = None
    ) -> str:
        handler = self.formatting_handlers.get(node.type)
        if not context:
            context = FormattingContext()
        if handler is None:
            raise TwaddleConversionError(
                f"No formatting handler registered for type {node.type}\n"
                f"Node has attributes: {node.attributes}"
            )
        tag = handler.format(node)
        if context.needs_space:
            tag = " " + tag
        return tag

    def format(
        self, node: POSNode, context: Optional[FormattingContext] = None
    ) -> FormattingContext:
        if not isinstance(node, POSNode):
            raise TwaddleConversionError("Input must be a POSNode")
        if not context:
            context = FormattingContext()
        twaddle_string = context.value
        if node.pre_punctuation:
            twaddle_string = node.pre_punctuation + twaddle_string

        if not node.children:
            context = FormattingContext(
                needs_space=context.needs_space,
                queued_punctuation=context.queued_punctuation,
            )
            twaddle_string += self.format_node(node, context)
        else:
            for child in node.children:
                if context.queued_punctuation:
                    twaddle_string += context.queued_punctuation
                    context.queued_punctuation = None
                twaddle_string += self.format(child, context).value
                context.needs_space = child.space_follows
                if child.post_punctuation:
                    context.queued_punctuation = child.post_punctuation
        if node.post_punctuation:
            context.queued_punctuation = node.post_punctuation
        return FormattingContext(
            value=twaddle_string,
            needs_space=context.needs_space,
            queued_punctuation=context.queued_punctuation,
        )

    def format_as_sentence(self, tree: POSNode) -> str:
        if not isinstance(tree, POSNode):
            raise TwaddleConversionError("Input must be a POSNode")
        top_level_context = self.format(tree)
        twaddle_string = top_level_context.value
        if top_level_context.queued_punctuation:
            twaddle_string += top_level_context.queued_punctuation
        result = f"[case:sentence]{twaddle_string}"
        logger.info(result)
        return result
