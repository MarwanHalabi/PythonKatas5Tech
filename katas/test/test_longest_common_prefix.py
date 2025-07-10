import unittest
from katas.longest_common_prefix import longest_common_prefix


class Testlonggest(unittest.TestCase):
    def test_longest_common_prefix(self):
        value = longest_common_prefix(["flower", "flow", "flight"])
        self.assertEqual(value, "fl")
