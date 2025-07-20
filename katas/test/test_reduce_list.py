import unittest
from katas.reduce_list import reduce_array


class TestReduce(unittest.TestCase):
    def test_longest_common_prefix(self):
        sample_list = [10, 15, 7, 20, 25]
        res = [10, 5, -8, 13, 5]
        reduce_array(sample_list)
        self.assertEqual(sample_list, res)
