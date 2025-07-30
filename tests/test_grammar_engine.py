import unittest
from greenideas.grammar_engine import GrammarEngine
from greenideas.exceptions import RuleNotFoundError
from greenideas.pos_types import POSType

class TestGrammarEngine(unittest.TestCase):

    def setUp(self):
        self.engine = GrammarEngine()

    def test_generate_tree_simple_case(self):
        self.engine.add_rule(POSType.S, [POSType.NP, POSType.VP])
        tree = self.engine.generate_tree(POSType.S)
        self.assertTrue(isinstance(tree, dict))
        self.assertIn(POSType.NP, tree[POSType.S])
        self.assertIn(POSType.VP, tree[POSType.S])

if __name__ == '__main__':
    unittest.main()