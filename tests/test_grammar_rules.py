from unittest import TestCase

from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.attributes.number import Number
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec


class TestGrammarRule(TestCase):
    def setUp(self):
        self.np__det_n = GrammarRule(
            SourceSpec(
                DefaultEnglishPOSType.NP, {AttributeType.NUMBER: Number.SINGULAR}
            ),
            [
                ExpansionSpec(
                    DefaultEnglishPOSType.Det, {AttributeType.NUMBER: Number.SINGULAR}
                ),
                ExpansionSpec(
                    DefaultEnglishPOSType.Det, {AttributeType.NUMBER: Number.SINGULAR}
                ),
            ],
            weight=1.0,
            ignore_after_depth=2,
        )

    def test_is_applicable_to_node_attribute_mismatch(self):
        node = POSNode(
            DefaultEnglishPOSType.NP,
            attributes={AttributeType.NUMBER: Number.PLURAL},
            depth=1,
        )
        self.assertFalse(self.np__det_n.is_applicable_to_node(node))

    def test_is_applicable_to_node_attribute_match(self):
        node = POSNode(
            DefaultEnglishPOSType.NP,
            attributes={AttributeType.NUMBER: Number.SINGULAR},
            depth=1,
        )
        self.assertTrue(self.np__det_n.is_applicable_to_node(node))

    def test_is_applicable_to_node_depth_exceeded(self):
        node = POSNode(
            DefaultEnglishPOSType.NP,
            attributes={AttributeType.NUMBER: Number.SINGULAR},
            depth=3,
        )
        self.assertFalse(self.np__det_n.is_applicable_to_node(node))
