import unittest

from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.attributes.number import Number
from greenideas.attributes.person import Person
from greenideas.attributes.tense import Tense
from greenideas.attributes.valency import Valency
from greenideas.parts_of_speech.default_english_pos_types import DefaultEnglishPOSType
from greenideas.parts_of_speech.pos_node import POSNode
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
        node = POSNode(type=DefaultEnglishPOSType.Verb)
        node.attributes.set(AttributeType.NUMBER, Number.SINGULAR)
        node.attributes.set(AttributeType.PERSON, Person.FIRST)
        node.attributes.set(AttributeType.TENSE, Tense.PAST)
        node.attributes.set(AttributeType.VALENCY, Valency.DIVALENT)
        tag = self.formatter.format_node(node)
        self.assertEqual(tag, "<verb-divalent.past>")

    def test_noun_tag(self):
        node = POSNode(type=DefaultEnglishPOSType.Noun)
        node.attributes.set(AttributeType.NUMBER, Number.PLURAL)
        node.attributes.set(AttributeType.CASE, Case.GENITIVE)
        tag = self.formatter.format_node(node)
        self.assertEqual(tag, "<noun.plgen>")

    def test_det_tag(self):
        node = POSNode(type=DefaultEnglishPOSType.Det)
        node.attributes.set(AttributeType.NUMBER, Number.SINGULAR)
        tag = self.formatter.format_node(node)
        self.assertEqual(tag, "<det.sg>")

    def test_prep_tag(self):
        node = POSNode(type=DefaultEnglishPOSType.Prep)
        tag = self.formatter.format_node(node)
        self.assertEqual(tag, "<prep>")

    def test_adj_tag(self):
        node = POSNode(type=DefaultEnglishPOSType.Adj)
        tag = self.formatter.format_node(node)
        self.assertEqual(tag, "<adj>")

    def test_adv_tag(self):
        node = POSNode(type=DefaultEnglishPOSType.Adv)
        tag = self.formatter.format_node(node)
        self.assertEqual(tag, "<adv>")

    def test_verb_bare_tag(self):
        node = POSNode(type=DefaultEnglishPOSType.Verb_Bare)
        node.attributes.set(AttributeType.VALENCY, Valency.MONOVALENT)
        tag = self.formatter.format_node(node)
        self.assertEqual(tag, "<verb-monovalent>")


if __name__ == "__main__":
    unittest.main()
