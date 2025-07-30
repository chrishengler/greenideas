import unittest

from greenideas.pos_node import POSNode
from greenideas.pos_types import POSType
from greenideas.tree_to_twaddle import TreeToTwaddle


class TestTreeToTwaddle(unittest.TestCase):

    def setUp(self):
        self.converter = TreeToTwaddle()

    def test_convert_tree_valid(self):
        det = POSNode(type_=POSType.Det)
        noun = POSNode(type_=POSType.Noun)
        verb = POSNode(type_=POSType.Verb)
        noun_phrase = POSNode(type_=POSType.NP, children=[det, noun])
        verb_phrase = POSNode(type_=POSType.VP, children=[verb, det, noun])
        sentence = POSNode(type_=POSType.S, children=[noun_phrase, verb_phrase])
        expected_template = "<det> <noun> <verb> <det> <noun>"
        result = self.converter.convert_tree(sentence)
        self.assertEqual(result, expected_template)


if __name__ == "__main__":
    unittest.main()
