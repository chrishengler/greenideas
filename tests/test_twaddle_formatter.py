import unittest

from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.number import Number
from greenideas.attributes.person import Person
from greenideas.attributes.tense import Tense
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
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
            type=POSType.Det, attributes={AttributeType.NUMBER: Number.SINGULAR}
        )
        noun = POSNode(
            type=POSType.Noun, attributes={AttributeType.NUMBER: Number.SINGULAR}
        )
        verb = POSNode(
            type=POSType.Verb,
            attributes={
                AttributeType.NUMBER: Number.SINGULAR,
                AttributeType.PERSON: Person.THIRD,
                AttributeType.TENSE: Tense.PRESENT,
            },
        )
        noun_phrase = POSNode(type=POSType.NP, children=[det, noun])
        verb_phrase = POSNode(type=POSType.VP, children=[verb, det, noun])
        sentence = POSNode(type=POSType.S, children=[noun_phrase, verb_phrase])
        expected_template = "<det.sg> <noun.sg> <verb.s> <det.sg> <noun.sg>"
        result = self.formatter.format(sentence)
        self.assertEqual(result, expected_template)


if __name__ == "__main__":
    unittest.main()
