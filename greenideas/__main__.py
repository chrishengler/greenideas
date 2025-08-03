import readline  # noqa: F401

from greenideas.grammar_engine import GrammarEngine
from greenideas.pos_types import POSType
from greenideas.rules.default_rules import default_rules
from greenideas.tree_to_twaddle import convert_tree


def main():
    engine = GrammarEngine()
    engine.add_ruleset(default_rules)
    tree = engine.generate_tree(POSType.S)
    print(tree)
    print(convert_tree(tree))


if __name__ == "__main__":
    main()
