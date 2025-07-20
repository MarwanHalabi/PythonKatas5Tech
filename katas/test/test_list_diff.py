import unittest
from katas.list_diff import find_difference


class TestListDiff(unittest.TestCase):
    def test_list_diff_empty_string(self):
        value = find_difference([])
        self.assertEqual(value, 0)

    def test_list_diff_both_postive_negative(self):
        value_1 = find_difference([1, -2, 3, -4, 5])
        value_2 = find_difference([1, -2, 3, 4, -6])

        self.assertEqual(value_1, 9)
        self.assertEqual(value_2, 10)

    def test_list_diff_same(self):
        value = value_2 = find_difference([1, 2, 3, 4, 6])
        self.assertEqual(value, 5) 