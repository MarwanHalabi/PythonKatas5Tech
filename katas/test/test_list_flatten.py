import unittest
from katas.list_flatten import flatten_list


class TestFlattenList(unittest.TestCase):
    def test_flatten_list(self):
        input_list = [[1,2,3], [4, [5, 6]], 7]
        value = flatten_list(input_list)
        self.assertEqual(value, [1, 2, 3, 4, 5, 6, 7])
