import unittest

from greenideas.grammar_engine import GrammarEngine
from greenideas.pos_types import POSType


class TestGrammarEngineAnnotationAgreement(unittest.TestCase):
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

    def test_subject_verb_agreement(self):
        tree = self.engine.generate_tree(POSType.S)
        self.engine.annotate_top_down(tree, {})
        subj_np = tree.children[0]
        verb = tree.children[1].children[0]
        self.assertEqual(
            subj_np.attributes.get("number"), verb.attributes.get("number")
        )
        self.assertEqual(
            subj_np.attributes.get("person"), verb.attributes.get("person")
        )

    def test_embedded_np_independent(self):
        # Add NP -> NP PP, PP -> Prep NP, Prep -> 'with'
        self.engine.add_rule(POSType.NP, [POSType.NP, POSType.PP])
        self.engine.add_rule(POSType.PP, [POSType.Prep, POSType.NP])
        self.engine.add_rule(POSType.Prep, ["with"])
        # Generate a tree with embedded NP
        tree = self.engine.generate_tree(POSType.S)
        self.engine.annotate_top_down(tree, {})
        # Find outer and inner NP
        outer_np = tree.children[0]
        # If the outer NP has children and the first is NP, that's the embedded NP
        if outer_np.children and outer_np.children[0].type == POSType.NP:
            inner_np = outer_np.children[0]
            self.assertIn(inner_np.attributes.get("number"), ["singular", "plural"])
            self.assertIn(outer_np.attributes.get("number"), ["singular", "plural"])
            # Not required to be equal
        else:
            self.skipTest("No embedded NP in this expansion.")


if __name__ == "__main__":
    unittest.main()
