import unittest

from greenideas.attributes.attribute_type import AttributeType
from greenideas.attributes.case import Case
from greenideas.exceptions import RuleNotFoundError
from greenideas.expansion_spec import INHERIT, ExpansionSpec
from greenideas.grammar_engine import GrammarEngine
from greenideas.pos_node import POSNode
from greenideas.pos_types import POSType
from greenideas.rules.grammar_rule import GrammarRule


class TestGrammarEngine(unittest.TestCase):
    def setUp(self):
        self.engine = GrammarEngine()
        # Define rules but do not add them yet
        # Added in tests as required
        self.s_rule = GrammarRule(
            POSType.S,
            [
                ExpansionSpec(
                    POSType.NP,
                    {AttributeType.NUMBER: INHERIT, AttributeType.PERSON: INHERIT},
                ),
                ExpansionSpec(
                    POSType.VP,
                    {AttributeType.NUMBER: INHERIT, AttributeType.PERSON: INHERIT},
                ),
            ],
        )
        self.np_rule = GrammarRule(
            POSType.NP,
            [
                ExpansionSpec(
                    POSType.Det,
                    {AttributeType.NUMBER: INHERIT, AttributeType.CASE: INHERIT},
                ),
                ExpansionSpec(
                    POSType.Noun,
                    {AttributeType.NUMBER: INHERIT, AttributeType.CASE: INHERIT},
                ),
            ],
        )
        self.vp_rule = GrammarRule(
            POSType.VP,
            [
                ExpansionSpec(
                    POSType.Verb,
                    {AttributeType.NUMBER: INHERIT, AttributeType.CASE: INHERIT},
                ),
                ExpansionSpec(
                    POSType.NP,
                    {
                        AttributeType.NUMBER: INHERIT,
                        AttributeType.CASE: Case.ACCUSATIVE,
                    },
                ),
            ],
        )
        self.pp_rule = GrammarRule(
            POSType.PP, [ExpansionSpec(POSType.Prep), ExpansionSpec(POSType.NP)]
        )
        self.simple_np_rule = GrammarRule(POSType.NP, [POSType.Det, POSType.Noun])
        self.simple_vp_rule = GrammarRule(POSType.VP, [POSType.Verb, POSType.NP])

    def test_agreement(self):
        self.engine.add_rule(self.s_rule)
        self.engine.add_rule(self.np_rule)
        self.engine.add_rule(self.vp_rule)
        tree = self.engine.generate_tree(POSType.S)
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
            part_of_speech=POSType.S,
            expansion=[
                ExpansionSpec(POSType.NP, {AttributeType.CASE: Case.GENITIVE}),
                ExpansionSpec(
                    POSType.NP,
                    {AttributeType.NUMBER: INHERIT, AttributeType.PERSON: INHERIT},
                ),
            ],
        )
        self.engine.add_rule(rule)
        tree = self.engine.generate_tree(POSType.S)
        child1, child2 = tree.children
        self.assertEqual(
            child1.attributes._values.get(AttributeType.CASE), Case.GENITIVE
        )
        self.assertEqual(
            child2.attributes.get(AttributeType.NUMBER),
            tree.attributes.get(AttributeType.NUMBER),
        )
        self.assertEqual(
            child2.attributes.get(AttributeType.PERSON),
            tree.attributes.get(AttributeType.PERSON),
        )

    def test_expand_to_tree_returns_posnode_with_posnode_children(self):
        self.engine.add_rule(self.s_rule)
        self.engine.add_rule(self.simple_np_rule)
        self.engine.add_rule(self.simple_vp_rule)
        tree = self.engine.generate_tree(POSType.S)
        self.assertIsInstance(tree, POSNode)
        self.assertEqual(tree.type, POSType.S)
        self.assertEqual(tree.children[0].type, POSType.NP)
        self.assertEqual(tree.children[1].type, POSType.VP)

    def test_grammar_class_add_and_get(self):
        self.engine.add_rule(self.pp_rule)
        rules = self.engine.grammar.get_rules(POSType.PP)
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules[0].expansion[0].pos_type, POSType.Prep)
        self.assertEqual(rules[0].expansion[1].pos_type, POSType.NP)

    def test_tree_generation_failure(self):
        # No rules added
        with self.assertRaises(RuleNotFoundError):
            self.engine.generate_tree(POSType.S)

    def test_initialization(self):
        engine = GrammarEngine()
        self.assertIsNotNone(engine)


if __name__ == "__main__":
    unittest.main()
