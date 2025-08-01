import unittest

from greenideas.attributes.attribute_type import AttributeType
from greenideas.grammar_engine import GrammarEngine
from greenideas.pos_node import POSNode
from greenideas.pos_types import POSType


class TestGrammarEngineAnnotation(unittest.TestCase):
    def setUp(self):
        self.engine = GrammarEngine()

    def test_attribute_propagation(self):
        # S -> NP VP; VP -> Verb
        noun = POSNode(type=POSType.Noun)
        verb = POSNode(type=POSType.Verb)
        np = POSNode(type=POSType.NP, children=[noun])
        vp = POSNode(type=POSType.VP, children=[verb])
        s = POSNode(type=POSType.S, children=[np, vp])
        self.engine.annotate_top_down(s)
        # NP and Verb and their children should both inherit number and person from S
        for elem in [np, vp, verb, noun]:
            self.assertEqual(
                elem.attributes.get(AttributeType.NUMBER),
                s.attributes.get(AttributeType.NUMBER),
            )
            self.assertEqual(
                elem.attributes.get(AttributeType.NUMBER),
                s.attributes.get(AttributeType.NUMBER),
            )

    def test_embedded_np(self):
        # S -> NP VP; NP -> NP PP; PP -> Prep NP
        inner_np = POSNode(type=POSType.NP)
        prep = POSNode(type=POSType.Prep)
        pp = POSNode(type=POSType.PP, children=[prep, inner_np])
        outer_np = POSNode(type=POSType.NP, children=[inner_np, pp])
        vp = POSNode(type=POSType.VP)
        s = POSNode(type=POSType.S, children=[outer_np, vp])
        self.engine.annotate_top_down(s)
        # Outer and inner NP may have different number/person
        self.assertIsNotNone(outer_np.attributes.get(AttributeType.NUMBER))
        self.assertIsNotNone(inner_np.attributes.get(AttributeType.NUMBER))
        # Not required to be equal
