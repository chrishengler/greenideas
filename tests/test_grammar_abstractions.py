import unittest

from greenideas.grammar_engine import GrammarEngine
from greenideas.pos_node import POSNode
from greenideas.pos_types import POSType


class TestGrammarEngineAbstractions(unittest.TestCase):
    def setUp(self):
        self.engine = GrammarEngine()
        # S -> NP VP
        self.engine.add_rule(POSType.S, [POSType.NP, POSType.VP])
        # NP -> Det Noun
        self.engine.add_rule(POSType.NP, [POSType.Det, POSType.Noun])
        # VP -> Verb NP
        self.engine.add_rule(POSType.VP, [POSType.Verb, POSType.NP])
        # Det -> 'the'
        self.engine.add_rule(POSType.Det, ["the"])
        # Noun -> (terminal, no further expansion)
        self.engine.add_rule(POSType.Noun, ["cat"])
        # Verb -> (terminal, no further expansion)
        self.engine.add_rule(POSType.Verb, ["sees"])

    def test_expand_to_tree_returns_posnode(self):
        tree = self.engine.generate_tree(POSType.S)
        self.assertIsInstance(tree, POSNode)
        self.assertEqual(tree.type, POSType.S)
        self.assertEqual(tree.children[0].type, POSType.NP)
        self.assertEqual(tree.children[1].type, POSType.VP)

    def test_terminal_nodes_are_posnodes(self):
        tree = self.engine.generate_tree(POSType.S)
        # Find a Det node
        det = tree.children[0].children[0]
        self.assertIsInstance(det, POSNode)
        self.assertEqual(det.type, POSType.Det)
        self.assertEqual(det.value, "the")

    def test_grammar_rule_class(self):
        # Check that rules are GrammarRule objects
        rules = self.engine.grammar.get_rules(POSType.NP)
        self.assertTrue(
            all(hasattr(rule, "lhs") and hasattr(rule, "rhs") for rule in rules)
        )

    def test_grammar_class_add_and_get(self):
        # Add a new rule and retrieve it
        self.engine.add_rule(POSType.PP, [POSType.Prep, POSType.NP])
        rules = self.engine.grammar.get_rules(POSType.PP)
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules[0].rhs, [POSType.Prep, POSType.NP])


if __name__ == "__main__":
    unittest.main()
