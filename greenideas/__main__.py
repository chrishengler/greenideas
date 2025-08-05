import readline  # noqa: F401

from greenideas.grammar_engine import GrammarEngine
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.default_rules import default_rules
from greenideas.twaddle.tree_to_twaddle import tree_to_twaddle

# from twaddle.runner import TwaddleRunner


def main():
    engine = GrammarEngine()
    engine.add_ruleset(default_rules)
    tree = engine.generate_tree(POSType.S)
    print(tree)
    print(tree_to_twaddle(tree))


if __name__ == "__main__":
    main()
