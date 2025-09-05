import unittest

from greenideas.exceptions import RuleNotFoundError
from greenideas.grammar_engine import GrammarEngine
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.rules.default_english_rules.attributes.case import Case
from greenideas.rules.default_english_rules.attributes.default_english_attribute_type import (
    DefaultEnglishAttributeType,
)
from greenideas.rules.default_english_rules.parts_of_speech.default_english_pos_types import (
    DefaultEnglishPOSType,
)
from greenideas.rules.expansion_spec import INHERIT, ExpansionSpec
from greenideas.rules.grammar_rule import GrammarRule
from greenideas.rules.grammar_ruleset import GrammarRuleset
from greenideas.rules.source_spec import SourceSpec


class TestGrammarEngine(unittest.TestCase):
    def setUp(self):
        def dummy_relevance(pos: DefaultEnglishPOSType):
            return [
                DefaultEnglishAttributeType.CASE,
                DefaultEnglishAttributeType.NUMBER,
                DefaultEnglishAttributeType.NPFORM,
                DefaultEnglishAttributeType.PERSON,
            ]

        self.dummy_relevance_check = dummy_relevance
        self.ruleset = GrammarRuleset(dummy_relevance)
        self.engine = GrammarEngine(self.ruleset)
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

        self.s_no_spaces = GrammarRule(
            SourceSpec(DefaultEnglishPOSType.S),
            [
                ExpansionSpec(DefaultEnglishPOSType.NP, space_follows=False),
                ExpansionSpec(DefaultEnglishPOSType.VP, space_follows=True),
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
            [
                ExpansionSpec(DefaultEnglishPOSType.Det),
                ExpansionSpec(DefaultEnglishPOSType.Noun),
            ],
        )
        self.simple_vp_rule = GrammarRule(
            SourceSpec(DefaultEnglishPOSType.VP),
            [
                ExpansionSpec(DefaultEnglishPOSType.Verb),
                ExpansionSpec(DefaultEnglishPOSType.NP),
            ],
        )

    def test_agreement(self):
        self.ruleset.add_rule(self.s_rule)
        self.ruleset.add_rule(self.np_rule)
        self.ruleset.add_rule(self.vp_rule)
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
        self.ruleset.add_rule(rule)
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
        self.ruleset.add_rule(self.s_rule)
        self.ruleset.add_rule(self.simple_np_rule)
        self.ruleset.add_rule(self.simple_vp_rule)
        tree = self.engine.generate_tree(DefaultEnglishPOSType.S)
        self.assertIsInstance(tree, POSNode)
        self.assertEqual(tree.type, DefaultEnglishPOSType.S)
        self.assertEqual(tree.children[0].type, DefaultEnglishPOSType.NP)
        self.assertEqual(tree.children[1].type, DefaultEnglishPOSType.VP)
        for child in tree.children:
            self.assertIsInstance(child, POSNode)
            for attr in child.attributes._values.keys():
                self.assertIn(attr, self.dummy_relevance_check(child.type))

    def test_tree_generation_failure(self):
        # No rules added
        with self.assertRaises(RuleNotFoundError):
            self.engine.generate_tree(DefaultEnglishPOSType.S)

    def test_spacing_rules_followed(self):
        self.ruleset.add_rule(self.s_no_spaces)
        tree = self.engine.generate_tree(DefaultEnglishPOSType.S)
        self.assertIsInstance(tree, POSNode)
        self.assertEqual(tree.type, DefaultEnglishPOSType.S)
        self.assertEqual(tree.children[0].type, DefaultEnglishPOSType.NP)
        self.assertEqual(tree.children[0].space_follows, False)
        self.assertEqual(tree.children[1].type, DefaultEnglishPOSType.VP)
        self.assertEqual(tree.children[1].space_follows, True)


if __name__ == "__main__":
    unittest.main()
