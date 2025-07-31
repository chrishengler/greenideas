import unittest

from greenideas.grammar_engine import GrammarEngine
from greenideas.pos_node import POSNode
from greenideas.pos_types import POSType


class TestGrammarEngineAnnotation(unittest.TestCase):
    def setUp(self):
        self.engine = GrammarEngine()

    def test_subject_verb_agreement(self):
        # S -> NP VP; VP -> Verb
        verb = POSNode(type_=POSType.Verb)
        np = POSNode(type_=POSType.NP)
        vp = POSNode(type_=POSType.VP, children=[verb])
        s = POSNode(type_=POSType.S, children=[np, vp])
        self.engine.annotate_top_down(s, {})
        # Subject NP and Verb should agree in person/number
        self.assertEqual(np.attributes.get("number"), verb.attributes.get("number"))
        self.assertEqual(np.attributes.get("person"), verb.attributes.get("person"))

    def test_embedded_np(self):
        # S -> NP VP; NP -> NP PP; PP -> Prep NP
        inner_np = POSNode(type_=POSType.NP)
        prep = POSNode(type_=POSType.Prep)
        pp = POSNode(type_=POSType.PP, children=[prep, inner_np])
        outer_np = POSNode(type_=POSType.NP, children=[inner_np, pp])
        vp = POSNode(type_=POSType.VP)
        s = POSNode(type_=POSType.S, children=[outer_np, vp])
        self.engine.annotate_top_down(s, {})
        # Outer and inner NP may have different number/person
        self.assertIn(outer_np.attributes.get("number"), ["singular", "plural"])
        self.assertIn(inner_np.attributes.get("number"), ["singular", "plural"])
        # Not required to be equal
