import unittest

from greenideas.exceptions import RuleNotFoundError
from greenideas.grammar_rules import GrammarRules
from greenideas.pos_types import POSType


class TestGrammarRules(unittest.TestCase):

    def setUp(self):
        self.grammar_rules = GrammarRules()

    def test_add_rule(self):
        self.grammar_rules.add_rule(POSType.NP, [POSType.Adj, POSType.Noun])
        rules = self.grammar_rules.rules[POSType.NP]
        self.assertIn([POSType.Adj, POSType.Noun], rules)

    def test_get_rules(self):
        self.grammar_rules.add_rule(POSType.NP, [POSType.Adj, POSType.Noun])
        rules = self.grammar_rules.get_rules(POSType.NP)
        self.assertIn([POSType.Adj, POSType.Noun], rules)

    def test_rule_not_found(self):
        with self.assertRaises(RuleNotFoundError):
            self.grammar_rules.get_rules("NonExistentRule")


if __name__ == "__main__":
    unittest.main()
