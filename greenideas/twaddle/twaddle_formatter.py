from greenideas.exceptions import TwaddleConversionError
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.twaddle_formatting_handler import TwaddleFormattingHandler


class TwaddleFormatter:
    def __init__(self):
        self.formatting_handlers: dict[POSType, TwaddleFormattingHandler] = dict()

    def register_formatting_handler(
        self, pos: POSType, handler: TwaddleFormattingHandler
    ):
        self.formatting_handlers[pos] = handler

    def format_node(self, node: POSNode) -> str:
        handler = self.formatting_handlers.get(node.type)
        if handler is None:
            raise TwaddleConversionError(
                f"No formatting handler registered for type {node.type}"
                f"Node has attributes: {node.attributes}"
            )
        return handler.format(node)

    def format(self, tree: POSNode) -> str:
        if not isinstance(tree, POSNode):
            raise TwaddleConversionError("Input must be a POSNode")
        twaddle_string = ""
        if not tree.children:
            twaddle_string = self.format_node(tree)
        else:
            child_tags = [self.format(child) for child in tree.children]
            twaddle_string = " ".join(filter(None, [twaddle_string, *child_tags]))
        return twaddle_string

    def format_as_sentence(self, tree: POSNode) -> str:
        if not isinstance(tree, POSNode):
            raise TwaddleConversionError("Input must be a POSNode")
        twaddle_string = self.format(tree)
        return f"[case:sentence]{twaddle_string}."
