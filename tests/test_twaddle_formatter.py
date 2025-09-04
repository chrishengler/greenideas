import unittest

from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.attributes.number import Number
from greenideas.rules.default_english_rules.attributes.person import Person
from greenideas.rules.default_english_rules.attributes.tense import Tense
from greenideas.rules.default_english_rules.attributes.valency import Valency
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
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
            attributes={DefaultEnglishAttributeType.NUMBER: Number.SINGULAR},
        )
        noun = POSNode(
            type=DefaultEnglishPOSType.Noun,
            attributes={DefaultEnglishAttributeType.NUMBER: Number.SINGULAR},
        )
        verb = POSNode(
            type=DefaultEnglishPOSType.Verb,
            attributes={
                DefaultEnglishAttributeType.NUMBER: Number.SINGULAR,
                DefaultEnglishAttributeType.PERSON: Person.THIRD,
                DefaultEnglishAttributeType.TENSE: Tense.PRESENT,
                DefaultEnglishAttributeType.VALENCY: Valency.MONOVALENT,
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
            attributes={DefaultEnglishAttributeType.NUMBER: Number.SINGULAR},
        )
        noun = POSNode(
            type=DefaultEnglishPOSType.Noun,
            attributes={DefaultEnglishAttributeType.NUMBER: Number.SINGULAR},
        )
        verb = POSNode(
            type=DefaultEnglishPOSType.Verb,
            attributes={
                DefaultEnglishAttributeType.NUMBER: Number.SINGULAR,
                DefaultEnglishAttributeType.PERSON: Person.THIRD,
                DefaultEnglishAttributeType.TENSE: Tense.PRESENT,
                DefaultEnglishAttributeType.VALENCY: Valency.MONOVALENT,
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
