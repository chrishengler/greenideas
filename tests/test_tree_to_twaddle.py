import unittest

from greenideas.pos_node import POSNode
from greenideas.pos_types import POSType
from greenideas.tree_to_twaddle import TreeToTwaddle


class TestTreeToTwaddle(unittest.TestCase):

    def setUp(self):
        self.converter = TreeToTwaddle()

    def test_convert_tree_valid(self):
        det = POSNode(type=POSType.Det)
        noun = POSNode(type=POSType.Noun)
        verb = POSNode(type=POSType.Verb)
        noun_phrase = POSNode(type=POSType.NP, children=[det, noun])
        verb_phrase = POSNode(type=POSType.VP, children=[verb, det, noun])
        sentence = POSNode(type=POSType.S, children=[noun_phrase, verb_phrase])
        expected_template = "<det> <noun> <verb> <det> <noun>"
        result = self.converter.convert_tree(sentence)
        self.assertEqual(result, expected_template)


if __name__ == "__main__":
    unittest.main()
