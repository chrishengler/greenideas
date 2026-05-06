import logging
import readline  # noqa: F401
import sys
from importlib.resources import files

from twaddle.runner import TwaddleRunner

from greenideas.grammar_engine import GrammarEngine
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.default_rules import default_rules
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.twaddle.default_formatters.default_formatting_handlers import (
    default_formatting_handlers,
)
from greenideas.twaddle.twaddle_formatter import TwaddleFormatter


def pretty_print_tree(tree: POSNode):
    indent = "\t" * tree.depth
    print(f'{indent}-{tree.type}: "{tree.twaddle_result}"')
    for child in tree.children:
        pretty_print_tree(child)


def main():
    logging.basicConfig(filename="greenideas.log", level=logging.INFO)
    if len(sys.argv) < 2:
        dictionary_path = files("greenideas.default_dictionary")
    else:
        dictionary_path = sys.argv[1]
    twaddle_runner = TwaddleRunner(dictionary_path, persistent_clipboard=True)

    engine = GrammarEngine(default_rules)
    tree = engine.generate_tree(DefaultEnglishPOSType.Utterance)
    print(tree)

    formatter = TwaddleFormatter()
    for type, handler in default_formatting_handlers.items():
        formatter.register_formatting_handler(type, handler)

    formatted_tree = formatter.format_as_sentence(tree)
    display_twaddle_string = formatted_tree.display_twaddle_string
    internal_twaddle_string = formatted_tree.internal_twaddle_string
    print(display_twaddle_string)
    print(twaddle_runner.run_sentence(internal_twaddle_string))
    formatter.fill_twaddle_results(tree, twaddle_runner)

    pretty_print_tree(tree)


if __name__ == "__main__":
    main()
