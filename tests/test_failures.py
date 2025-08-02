import pytest

from greenideas.exceptions import RuleNotFoundError
from greenideas.grammar_engine import GrammarEngine
from greenideas.pos_types import POSType


def test_grammar_engine_initialization():
    engine = GrammarEngine()
    assert engine is not None


def test_tree_generation_failure():
    engine = GrammarEngine()
    engine.rules = {}
    with pytest.raises(RuleNotFoundError):
        engine.generate_tree(POSType.S)


def test_twaddle_template_failure():
    from greenideas.tree_to_twaddle import TreeToTwaddle

    converter = TreeToTwaddle()
    tree = "invalid_tree_structure"
    with pytest.raises(ValueError):
        converter.convert_tree(tree)
