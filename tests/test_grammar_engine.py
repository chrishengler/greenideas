import unittest

from greenideas.exceptions import RuleNotFoundError
from greenideas.grammar_engine import GrammarEngine
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.attributes.case import Case
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_attributes import (
    relevant_attributes,
)
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.source_spec import SourceSpec


class TestGrammarEngine(unittest.TestCase):
    def setUp(self):
        self.engine = GrammarEngine()
        # Define rules but do not add them yet
        # Added in tests as required
        self.s_rule = GrammarRule(
            SourceSpec(DefaultEnglishPOSType.S),
            [
                ExpansionSpec(
                    DefaultEnglishPOSType.NP,
                    {
                        DefaultEnglishAttributeType.NUMBER: INHERIT,
                        DefaultEnglishAttributeType.PERSON: INHERIT,
                    },
                ),
                ExpansionSpec(
                    DefaultEnglishPOSType.VP,
                    {
                        DefaultEnglishAttributeType.NUMBER: INHERIT,
                        DefaultEnglishAttributeType.PERSON: INHERIT,
                    },
                ),
            ],
        )
        self.np_rule = GrammarRule(
            SourceSpec(DefaultEnglishPOSType.NP),
            [
                ExpansionSpec(
                    DefaultEnglishPOSType.Det,
                    {
                        DefaultEnglishAttributeType.NUMBER: INHERIT,
                        DefaultEnglishAttributeType.CASE: INHERIT,
                    },
                ),
                ExpansionSpec(
                    DefaultEnglishPOSType.Noun,
                    {
                        DefaultEnglishAttributeType.NUMBER: INHERIT,
                        DefaultEnglishAttributeType.CASE: INHERIT,
                    },
                ),
            ],
        )
        self.vp_rule = GrammarRule(
            SourceSpec(DefaultEnglishPOSType.VP),
            [
                ExpansionSpec(
                    DefaultEnglishPOSType.Verb,
                    {DefaultEnglishAttributeType.NUMBER: INHERIT},
                ),
                ExpansionSpec(
                    DefaultEnglishPOSType.NP,
                    {
                        DefaultEnglishAttributeType.NUMBER: INHERIT,
                        DefaultEnglishAttributeType.CASE: Case.OBJECTIVE,
                    },
                ),
            ],
        )
        self.pp_rule = GrammarRule(
            SourceSpec(DefaultEnglishPOSType.PP),
            [
                ExpansionSpec(DefaultEnglishPOSType.Prep),
                ExpansionSpec(DefaultEnglishPOSType.NP),
            ],
        )
        self.simple_np_rule = GrammarRule(
            SourceSpec(DefaultEnglishPOSType.NP),
            [DefaultEnglishPOSType.Det, DefaultEnglishPOSType.Noun],
        )
        self.simple_vp_rule = GrammarRule(
            SourceSpec(DefaultEnglishPOSType.VP),
            [DefaultEnglishPOSType.Verb, DefaultEnglishPOSType.NP],
        )

    def test_agreement(self):
        self.engine.add_rule(self.s_rule)
        self.engine.add_rule(self.np_rule)
        self.engine.add_rule(self.vp_rule)
        tree = self.engine.generate_tree(DefaultEnglishPOSType.S)
        subj_np = tree.children[0]
        verb = tree.children[1].children[0]
        self.assertEqual(
            subj_np.attributes.get("number"), verb.attributes.get("number")
        )
        self.assertEqual(
            subj_np.attributes.get("person"), verb.attributes.get("person")
        )

    def test_case_constraint(self):
        rule = GrammarRule(
            SourceSpec(DefaultEnglishPOSType.S),
            [
                ExpansionSpec(
                    DefaultEnglishPOSType.NP,
                    {DefaultEnglishAttributeType.CASE: Case.GENITIVE},
                ),
                ExpansionSpec(
                    DefaultEnglishPOSType.NP,
                    {
                        DefaultEnglishAttributeType.NUMBER: INHERIT,
                        DefaultEnglishAttributeType.PERSON: INHERIT,
                    },
                ),
            ],
        )
        self.engine.add_rule(rule)
        tree = self.engine.generate_tree(DefaultEnglishPOSType.S)
        child1, child2 = tree.children
        self.assertEqual(
            child1.attributes._values.get(DefaultEnglishAttributeType.CASE),
            Case.GENITIVE,
        )
        self.assertEqual(
            child2.attributes.get(DefaultEnglishAttributeType.NUMBER),
            tree.attributes.get(DefaultEnglishAttributeType.NUMBER),
        )
        self.assertEqual(
            child2.attributes.get(DefaultEnglishAttributeType.PERSON),
            tree.attributes.get(DefaultEnglishAttributeType.PERSON),
        )

    def test_expand_to_tree_returns_posnode_with_posnode_children(self):
        self.engine.add_rule(self.s_rule)
        self.engine.add_rule(self.simple_np_rule)
        self.engine.add_rule(self.simple_vp_rule)
        tree = self.engine.generate_tree(DefaultEnglishPOSType.S)
        self.assertIsInstance(tree, POSNode)
        self.assertEqual(tree.type, DefaultEnglishPOSType.S)
        self.assertEqual(tree.children[0].type, DefaultEnglishPOSType.NP)
        self.assertEqual(tree.children[1].type, DefaultEnglishPOSType.VP)
        for child in tree.children:
            self.assertIsInstance(child, POSNode)
            for attr in child.attributes._values.keys():
                self.assertIn(attr, relevant_attributes(child.type))

    def test_grammar_class_add_and_get(self):
        self.engine.add_rule(self.pp_rule)
        rules = self.engine.grammar.get_rules(DefaultEnglishPOSType.PP)
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules[0].expansion[0].pos_type, DefaultEnglishPOSType.Prep)
        self.assertEqual(rules[0].expansion[1].pos_type, DefaultEnglishPOSType.NP)

    def test_tree_generation_failure(self):
        # No rules added
        with self.assertRaises(RuleNotFoundError):
            self.engine.generate_tree(DefaultEnglishPOSType.S)

    def test_initialization(self):
        engine = GrammarEngine()
        self.assertIsNotNone(engine)


if __name__ == "__main__":
    unittest.main()
