import unittest

from greenideas.twaddle.twaddle_tag import build_twaddle_tag


class TestTwaddleTagBuilder(unittest.TestCase):
    def test_build_tag_without_attributes(self):
        tag = build_twaddle_tag("test")
        self.assertEqual(tag, "<test>")

    def test_build_tag_with_class_specifier(self):
        tag = build_twaddle_tag("test", class_specifier="class")
        self.assertEqual(tag, "<test-class>")

    def test_build_tag_with_form(self):
        tag = build_twaddle_tag("test", form="form")
        self.assertEqual(tag, "<test.form>")

    def test_build_tag_with_class_and_form(self):
        tag = build_twaddle_tag("dict", "class", "form")
        self.assertEqual(tag, "<dict-class.form>")

    def test_build_tag_with_multiple_class_specifiers(self):
        tag = build_twaddle_tag("dict", class_specifier=["class1", "class2"])
        self.assertEqual(tag, "<dict-class1-class2>")
