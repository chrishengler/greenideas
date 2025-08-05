import unittest

from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.attributes.number import Number
from greenideas.attributes.person import Person
from greenideas.attributes.tense import Tense
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.twaddle.default_formatters.default_formatting_handlers import (
    default_formatting_handlers,
)
from greenideas.twaddle.twaddle_formatter import TwaddleFormatter


class TestDefaultTwaddleFormatters(unittest.TestCase):
    def setUp(self):
        self.formatter = TwaddleFormatter()
        for type, handler in default_formatting_handlers.items():
            self.formatter.register_formatting_handler(type, handler)

    def test_verb_tag(self):
        node = POSNode(type=POSType.Verb)
        node.attributes.set(AttributeType.NUMBER, Number.SINGULAR)
        node.attributes.set(AttributeType.PERSON, Person.FIRST)
        node.attributes.set(AttributeType.TENSE, Tense.PRESENT)
        tag = self.formatter.format_node(node)
        self.assertEqual(tag, "<verb.1sgpres>")

    def test_noun_tag(self):
        node = POSNode(type=POSType.Noun)
        node.attributes.set(AttributeType.NUMBER, Number.PLURAL)
        node.attributes.set(AttributeType.CASE, Case.GENITIVE)
        tag = self.formatter.format_node(node)
        self.assertEqual(tag, "<noun.plgen>")

    def test_det_tag(self):
        node = POSNode(type=POSType.Det)
        node.attributes.set(AttributeType.NUMBER, Number.SINGULAR)
        tag = self.formatter.format_node(node)
        self.assertEqual(tag, "<det.sg>")

    def test_prep_tag(self):
        node = POSNode(type=POSType.Prep)
        tag = self.formatter.format_node(node)
        self.assertEqual(tag, "<prep>")

    def test_adj_tag(self):
        node = POSNode(type=POSType.Adj)
        tag = self.formatter.format_node(node)
        self.assertEqual(tag, "<adj>")

    def test_adv_tag(self):
        node = POSNode(type=POSType.Adv)
        tag = self.formatter.format_node(node)
        self.assertEqual(tag, "<adv>")

    def test_verb_bare_tag(self):
        node = POSNode(type=POSType.Verb_Bare)
        tag = self.formatter.format_node(node)
        self.assertEqual(tag, "<verb>")


if __name__ == "__main__":
    unittest.main()
