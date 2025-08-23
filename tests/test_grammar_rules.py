from unittest import TestCase

from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.number import Number
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType
from greenideas.rules.expansion_spec import ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec


class TestGrammarRule(TestCase):
    def setUp(self):
        self.np__det_n = GrammarRule(
            SourceSpec(POSType.NP, {AttributeType.NUMBER: Number.SINGULAR}),
            [
                ExpansionSpec(POSType.Det, {AttributeType.NUMBER: Number.SINGULAR}),
                ExpansionSpec(POSType.Det, {AttributeType.NUMBER: Number.SINGULAR}),
            ],
            weight=1.0,
            ignore_after_depth=2,
        )

    def test_is_applicable_to_node_attribute_mismatch(self):
        node = POSNode(
            POSType.NP, attributes={AttributeType.NUMBER: Number.PLURAL}, depth=1
        )
        self.assertFalse(self.np__det_n.is_applicable_to_node(node))

    def test_is_applicable_to_node_attribute_match(self):
        node = POSNode(
            POSType.NP, attributes={AttributeType.NUMBER: Number.SINGULAR}, depth=1
        )
        self.assertTrue(self.np__det_n.is_applicable_to_node(node))

    def test_is_applicable_to_node_depth_exceeded(self):
        node = POSNode(
            POSType.NP, attributes={AttributeType.NUMBER: Number.SINGULAR}, depth=3
        )
        self.assertFalse(self.np__det_n.is_applicable_to_node(node))
