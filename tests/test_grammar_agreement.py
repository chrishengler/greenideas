import unittest

from greenideas.grammar_engine import GrammarEngine
from greenideas.grammar_rule import GrammarRule
from greenideas.pos_types import POSType


class TestGrammarEngineAnnotationAgreement(unittest.TestCase):
    def setUp(self):
        self.engine = GrammarEngine()
        # S -> NP VP
        self.engine.add_rule(GrammarRule(POSType.S, [POSType.NP, POSType.VP]))
        # NP -> Det Noun
        self.engine.add_rule(GrammarRule(POSType.NP, [POSType.Det, POSType.Noun]))
        # VP -> Verb NP
        self.engine.add_rule(GrammarRule(POSType.VP, [POSType.Verb, POSType.NP]))

    def test_subject_verb_agreement(self):
        tree = self.engine.generate_tree(POSType.S)
        self.engine.annotate_top_down(tree)
        subj_np = tree.children[0]
        verb = tree.children[1].children[0]
        self.assertEqual(
            subj_np.attributes.get("number"), verb.attributes.get("number")
        )
        self.assertEqual(
            subj_np.attributes.get("person"), verb.attributes.get("person")
        )

    def test_embedded_np(self):
        # Can't actually test this yet until we start selecting rules randomly
        # Add NP -> NP PP, PP -> Prep NP
        # self.engine.add_rule(GrammarRule(POSType.NP, [POSType.NP, POSType.PP]))
        # self.engine.add_rule(GrammarRule(POSType.PP, [POSType.Prep, POSType.NP]))
        # # Generate a tree with embedded NP
        # tree = self.engine.generate_tree(POSType.S)
        # self.
        # self.engine.annotate_top_down(tree, {})
        # print(tree)
        # # Find outer and inner NP
        # outer_np = tree.children[0]
        # # If the outer NP has children and the first is NP, that's the embedded NP
        # print(outer_np)
        # if outer_np.children and outer_np.children[0].type == POSType.NP:
        #     inner_np = outer_np.children[0]
        #     self.assertIn(inner_np.attributes.get("number"), ["singular", "plural"])
        #     self.assertIn(outer_np.attributes.get("number"), ["singular", "plural"])
        #     # Not required to be equal
        # else:
        self.skipTest("Can't test this yet")


if __name__ == "__main__":
    unittest.main()
