import unittest

from greenideas.attributes.attribute_type import AttributeType
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


class TestTwaddleFormatter(unittest.TestCase):

    def setUp(self):
        self.formatter = TwaddleFormatter()
        for type, handler in default_formatting_handlers.items():
            self.formatter.register_formatting_handler(type, handler)

    def test_convert_tree_valid(self):
        det = POSNode(
            type=DefaultEnglishPOSType.Det,
            attributes={AttributeType.NUMBER: Number.SINGULAR},
        )
        noun = POSNode(
            type=DefaultEnglishPOSType.Noun,
            attributes={AttributeType.NUMBER: Number.SINGULAR},
        )
        verb = POSNode(
            type=DefaultEnglishPOSType.Verb,
            attributes={
                AttributeType.NUMBER: Number.SINGULAR,
                AttributeType.PERSON: Person.THIRD,
                AttributeType.TENSE: Tense.PRESENT,
                AttributeType.VALENCY: Valency.MONOVALENT,
            },
        )
        noun_phrase = POSNode(type=DefaultEnglishPOSType.NP, children=[det, noun])
        verb_phrase = POSNode(type=DefaultEnglishPOSType.VP, children=[verb, det, noun])
        sentence = POSNode(
            type=DefaultEnglishPOSType.S, children=[noun_phrase, verb_phrase]
        )
        expected_template = "<det.sg> <noun.sg> <verb-monovalent.s> <det.sg> <noun.sg>"
        result = self.formatter.format(sentence)
        self.assertEqual(result, expected_template)

    def test_format_as_sentence(self):
        det = POSNode(
            type=DefaultEnglishPOSType.Det,
            attributes={AttributeType.NUMBER: Number.SINGULAR},
        )
        noun = POSNode(
            type=DefaultEnglishPOSType.Noun,
            attributes={AttributeType.NUMBER: Number.SINGULAR},
        )
        verb = POSNode(
            type=DefaultEnglishPOSType.Verb,
            attributes={
                AttributeType.NUMBER: Number.SINGULAR,
                AttributeType.PERSON: Person.THIRD,
                AttributeType.TENSE: Tense.PRESENT,
                AttributeType.VALENCY: Valency.MONOVALENT,
            },
        )
        noun_phrase = POSNode(type=DefaultEnglishPOSType.NP, children=[det, noun])
        verb_phrase = POSNode(type=DefaultEnglishPOSType.VP, children=[verb, det, noun])
        sentence = POSNode(
            type=DefaultEnglishPOSType.S, children=[noun_phrase, verb_phrase]
        )
        expected_template = (
            "[case:sentence]<det.sg> <noun.sg> <verb-monovalent.s> <det.sg> <noun.sg>."
        )
        result = self.formatter.format_as_sentence(sentence)
        self.assertEqual(result, expected_template)


if __name__ == "__main__":
    unittest.main()
