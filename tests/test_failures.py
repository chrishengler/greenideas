import pytest

from greenideas.exceptions import RuleNotFoundError, TwaddleConversionError
from greenideas.grammar_engine import GrammarEngine
from greenideas.parts_of_speech.default_english_pos_types import DefaultEnglishPOSType
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.twaddle.twaddle_formatter import TwaddleFormatter


def test_grammar_engine_initialization():
    engine = GrammarEngine()
    assert engine is not None


def test_tree_generation_failure():
    engine = GrammarEngine()
    engine.rules = {}
    with pytest.raises(RuleNotFoundError):
        engine.generate_tree(DefaultEnglishPOSType.S)


def test_twaddle_template_failure():
    tree = "not_a_pos_node"
    formatter = TwaddleFormatter()
    with pytest.raises(TwaddleConversionError):
        formatter.format(tree)


def test_twaddle_conversion_error():
    node = POSNode(DefaultEnglishPOSType.S)
    formatter = TwaddleFormatter()
    with pytest.raises(TwaddleConversionError):
        formatter.format(node)
