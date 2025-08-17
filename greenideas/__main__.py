import logging
import readline  # noqa: F401
import sys
from importlib.resources import files

from twaddle.runner import TwaddleRunner

from greenideas.grammar_engine import GrammarEngine
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.default_english_rules.default_rules import default_rules
from greenideas.twaddle.default_formatters.default_formatting_handlers import (
    default_formatting_handlers,
)
from greenideas.twaddle.twaddle_formatter import TwaddleFormatter


def main():
    logging.basicConfig(filename="greenideas.log", level=logging.INFO)
    if len(sys.argv) < 2:
        dictionary_path = files("greenideas.default_dictionary")
    else:
        dictionary_path = sys.argv[1]
    twaddle_runner = TwaddleRunner(dictionary_path)

    engine = GrammarEngine()
    engine.add_ruleset(default_rules)
    tree = engine.generate_tree(POSType.S)
    print(tree)

    formatter = TwaddleFormatter()
    for type, handler in default_formatting_handlers.items():
        formatter.register_formatting_handler(type, handler)

    twaddle_string = formatter.format_as_sentence(tree)
    print(twaddle_string)
    print(twaddle_runner.run_sentence(twaddle_string))


if __name__ == "__main__":
    main()
