import unittest

from greenideas.attributes.attribute_type import AttributeType
from greenideas.parts_of_speech.pos_node import POSNode
from greenideas.parts_of_speech.pos_types import POSType


class TestPOSNodeRelevantattributes(unittest.TestCase):
    def test_noun_relevant_attributes(self):
        node = POSNode(type=POSType.Noun)
        relevant = node.relevant_attributes
        self.assertIn(AttributeType.NUMBER, relevant)
        self.assertIn(AttributeType.CASE, relevant)
        self.assertNotIn(AttributeType.TENSE, relevant)
        self.assertNotIn(AttributeType.PERSON, relevant)

    def test_verb_relevant_attributes(self):
        node = POSNode(type=POSType.Verb)
        relevant = node.relevant_attributes
        self.assertIn(AttributeType.NUMBER, relevant)
        self.assertIn(AttributeType.PERSON, relevant)
        self.assertIn(AttributeType.TENSE, relevant)
        self.assertNotIn(AttributeType.CASE, relevant)

    def test_sentence_relevant_attributes(self):
        node = POSNode(type=POSType.S)
        relevant = node.relevant_attributes
        self.assertIn(AttributeType.NUMBER, relevant)
        self.assertIn(AttributeType.PERSON, relevant)
        self.assertIn(AttributeType.TENSE, relevant)
        self.assertNotIn(AttributeType.CASE, relevant)

    def test_det_relevant_attributes(self):
        node = POSNode(type=POSType.Det)
        relevant = node.relevant_attributes
        self.assertIn(AttributeType.NUMBER, relevant)
        self.assertIn(AttributeType.CASE, relevant)
        self.assertNotIn(AttributeType.TENSE, relevant)

    def test_prep_relevant_attributes(self):
        node = POSNode(type=POSType.Prep)
        relevant = node.relevant_attributes
        self.assertEqual(relevant, set())


if __name__ == "__main__":
    unittest.main()
