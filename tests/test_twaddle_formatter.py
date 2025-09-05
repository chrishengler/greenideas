import unittest

from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.attributes.animacy import Animacy
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
        result = self.formatter.format(sentence).value
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
            type=DefaultEnglishPOSType.S,
            children=[noun_phrase, verb_phrase],
            post_punctuation=".",
        )
        expected_template = (
            "[case:sentence]<det.sg> <noun.sg> <verb-monovalent.s> <det.sg> <noun.sg>."
        )
        result = self.formatter.format_as_sentence(sentence)
        self.assertEqual(result, expected_template)

    def test_format_with_and_without_spacing(self):
        det = POSNode(
            type=DefaultEnglishPOSType.Det,
            attributes={DefaultEnglishAttributeType.NUMBER: Number.SINGULAR},
        )
        noun = POSNode(
            type=DefaultEnglishPOSType.Noun,
            attributes={DefaultEnglishAttributeType.NUMBER: Number.SINGULAR},
            space_follows=False,
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
        sentence = POSNode(type=DefaultEnglishPOSType.S, children=[det, noun, verb])
        expected_template = "[case:sentence]<det.sg> <noun.sg><verb-monovalent.s>"
        result = self.formatter.format_as_sentence(sentence)
        self.assertEqual(result, expected_template)

    def test_format_single_node_with_punctuation(self):
        node = POSNode(
            type=DefaultEnglishPOSType.Noun,
            attributes={DefaultEnglishAttributeType.NUMBER: Number.PLURAL},
            pre_punctuation="...",
            post_punctuation="!",
        )
        expected_template = "[case:sentence]...<noun.pl>!"
        result = self.formatter.format_as_sentence(node)
        self.assertEqual(result, expected_template)

    def test_terminal_punctuation_not_top_level(self):
        verb = POSNode(
            type=DefaultEnglishPOSType.Verb,
            attributes={
                DefaultEnglishAttributeType.NUMBER: Number.SINGULAR,
                DefaultEnglishAttributeType.PERSON: Person.THIRD,
                DefaultEnglishAttributeType.TENSE: Tense.PRESENT,
                DefaultEnglishAttributeType.VALENCY: Valency.MONOVALENT,
            },
            post_punctuation="!",
        )
        sentence = POSNode(type=DefaultEnglishPOSType.S, children=[verb])
        expected_template = "[case:sentence]<verb-monovalent.s>!"
        result = self.formatter.format_as_sentence(sentence)
        self.assertEqual(result, expected_template)

    def test_with_spacing_and_punctuation(self):
        det = POSNode(
            type=DefaultEnglishPOSType.Det,
            attributes={DefaultEnglishAttributeType.NUMBER: Number.SINGULAR},
            pre_punctuation="!",
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
            pre_punctuation=",",
            post_punctuation="!",
        )
        sentence = POSNode(type=DefaultEnglishPOSType.S, children=[det, noun, verb])
        expected_template = "[case:sentence]!<det.sg> <noun.sg>, <verb-monovalent.s>!"
        result = self.formatter.format_as_sentence(sentence)
        self.assertEqual(result, expected_template)

    def test_punctuation_and_spacing_defined_on_intermediate_nodes(self):
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
        noun_phrase = POSNode(
            type=DefaultEnglishPOSType.NP, children=[det, noun], pre_punctuation="!"
        )
        verb_phrase = POSNode(
            type=DefaultEnglishPOSType.VP,
            children=[verb, det, noun],
            pre_punctuation=",",
            post_punctuation="?",
        )
        sentence = POSNode(
            type=DefaultEnglishPOSType.S,
            children=[noun_phrase, verb_phrase],
        )
        expected_template = "[case:sentence]!<det.sg> <noun.sg>, <verb-monovalent.s> <det.sg> <noun.sg>?"
        result = self.formatter.format_as_sentence(sentence)
        self.assertEqual(result, expected_template)

    def test_post_punctuation_pileup(self):
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
        rel_pron = POSNode(
            type=DefaultEnglishPOSType.RelativePron,
            attributes={DefaultEnglishAttributeType.ANIMACY: Animacy.ANIMATE},
        )
        rel_clause_verb = POSNode(
            type=DefaultEnglishPOSType.Verb,
            attributes={
                DefaultEnglishAttributeType.NUMBER: Number.SINGULAR,
                DefaultEnglishAttributeType.PERSON: Person.THIRD,
                DefaultEnglishAttributeType.TENSE: Tense.PAST,
                DefaultEnglishAttributeType.VALENCY: Valency.MONOVALENT,
            },
        )
        rel_clause = POSNode(
            type=DefaultEnglishPOSType.RelClause,
            children=[rel_pron, rel_clause_verb],
            pre_punctuation=",",
            post_punctuation=",",
        )
        noun_phrase = POSNode(type=DefaultEnglishPOSType.NP, children=[det, noun])
        noun_phrase_with_rel_clause = POSNode(
            type=DefaultEnglishPOSType.NP, children=[det, noun, rel_clause]
        )
        verb_phrase = POSNode(
            type=DefaultEnglishPOSType.VP,
            children=[verb, noun_phrase_with_rel_clause],
        )

        rel_clause = POSNode(
            type=DefaultEnglishPOSType.RelClause,
        )
        sentence = POSNode(
            type=DefaultEnglishPOSType.S,
            children=[noun_phrase, verb_phrase],
            post_punctuation=".",
        )
        result = self.formatter.format_as_sentence(sentence)
        expected_template = (
            "[case:sentence]<det.sg> <noun.sg> <verb-monovalent.s> <det.sg> "
            "<noun.sg>, <rel-animate> <verb-monovalent.past>."
        )
        self.assertEqual(result, expected_template)


if __name__ == "__main__":
    unittest.main()
