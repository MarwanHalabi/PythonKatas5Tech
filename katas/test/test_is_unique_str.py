import unittest
from katas.is_unique_str import is_unique


class TestIsUnique(unittest.TestCase):
    def test_is_unique_empty_string(self):
        self.assertTrue(is_unique(""))

    def test_is_unique_single_character(self):
        self.assertTrue(is_unique("a"))

    def test_is_unique_all_unique_characters(self):
        self.assertTrue(is_unique("abcdefg"))

    def test_is_unique_with_repeated_characters(self):
        self.assertFalse(is_unique("hello"))

    def test_is_unique_with_mixed_case(self):
        self.assertTrue(is_unique("AbCdeF"))
        self.assertTrue(is_unique("AaBbCc"))       