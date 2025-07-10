import unittest
from katas.sum_of_digits import sum_of_digits


class TestSuOfDigits(unittest.TestCase):
    def sum_of_digits(self):
        input1 = "abc123"
        value = sum_of_digits(input1)
        self.assertEqual(value, 6)
