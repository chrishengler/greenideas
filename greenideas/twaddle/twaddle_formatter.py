import logging
from typing import Optional

from twaddle import TwaddleException, TwaddleRunner

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

    def _add_sentence_case(self, twaddle_string: str) -> str:
        return f"[case:sentence]{twaddle_string}"

    def _add_copy(self, twaddle_string: str, node: POSNode) -> str:
        return f"[copy:{id(node)}]{{{twaddle_string}}}"

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
        return tag

    def format(
        self, node: POSNode, context: Optional[FormattingContext] = None
    ) -> FormattingContext:
        if not isinstance(node, POSNode):
            raise TwaddleConversionError("Input must be a POSNode")
        if not context:
            context = FormattingContext()
        display_twaddle_string = context.display_twaddle_string
        internal_twaddle_string = context.internal_twaddle_string

        if not node.children:
            context = FormattingContext(
                needs_space=context.needs_space,
                queued_punctuation=context.queued_punctuation,
            )
            formatted_node = self.format_node(node, context)
            if context.needs_space:
                formatted_node = " " + formatted_node
            display_twaddle_string += formatted_node
            internal_twaddle_string = formatted_node
        else:
            for child in node.children:
                if context.queued_punctuation:
                    display_twaddle_string += context.queued_punctuation
                    context.queued_punctuation = None
                formatted_child = self.format(child, context)
                copied_child = self._add_copy(
                    formatted_child.internal_twaddle_string, child
                )
                display_twaddle_string += formatted_child.display_twaddle_string
                internal_twaddle_string += copied_child
                context.needs_space = child.space_follows
                if child.post_punctuation:
                    context.queued_punctuation = child.post_punctuation
        if node.pre_punctuation:
            display_twaddle_string = node.pre_punctuation + display_twaddle_string
            internal_twaddle_string = node.pre_punctuation + internal_twaddle_string
        if node.post_punctuation:
            context.queued_punctuation = node.post_punctuation
        return FormattingContext(
            display_twaddle_string=display_twaddle_string,
            internal_twaddle_string=internal_twaddle_string,
            needs_space=context.needs_space,
            queued_punctuation=context.queued_punctuation,
        )

    def get_trimmed_sentence(self, node: POSNode, runner: TwaddleRunner) -> str:
        return runner.run_sentence(f"[paste:{id(node)}]").strip()

    def fill_twaddle_results(self, tree: POSNode, runner: TwaddleRunner):
        try:
            if not tree.twaddle_result:
                tree.twaddle_result = self.get_trimmed_sentence(tree, runner)
            for child in tree.children:
                child.twaddle_result = self.get_trimmed_sentence(child, runner)
                self.fill_twaddle_results(child, runner)
        except TwaddleException as e:
            print(f"error: {str(e)}")
            logger.error(f"Encountered an error filling Twaddle results: {str(e)}")

    def format_as_sentence(self, tree: POSNode) -> FormattingContext:
        if not isinstance(tree, POSNode):
            raise TwaddleConversionError("Input must be a POSNode")
        context = self.format(tree)
        context.display_twaddle_string = self._add_sentence_case(
            context.display_twaddle_string
        )
        context.internal_twaddle_string = self._add_sentence_case(
            context.internal_twaddle_string
        )
        if context.queued_punctuation:
            context.display_twaddle_string += context.queued_punctuation
            context.internal_twaddle_string += context.queued_punctuation
        context.internal_twaddle_string = self._add_copy(
            context.internal_twaddle_string, tree
        )
        return context
