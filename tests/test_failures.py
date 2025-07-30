import pytest

from greenideas.exceptions import RuleNotFoundError
from greenideas.grammar_engine import GrammarEngine


def test_grammar_engine_initialization():
    engine = GrammarEngine()
    assert engine is not None


def test_tree_generation_failure():
    engine = GrammarEngine()
    # Assuming generate_tree can fail if no rules are defined
    engine.rules = {}  # Clear rules to simulate failure
    with pytest.raises(RuleNotFoundError):
        engine.generate_tree("S")  # Attempt to generate a tree with no rules


def test_twaddle_template_failure():
    from greenideas.tree_to_twaddle import TreeToTwaddle

    converter = TreeToTwaddle()
    tree = "invalid_tree_structure"  # Simulate an invalid tree structure
    with pytest.raises(ValueError):
        converter.convert_tree(tree)  # Attempt to convert an invalid tree
