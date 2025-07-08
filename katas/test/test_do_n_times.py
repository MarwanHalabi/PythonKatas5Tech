import unittest
from unittest.mock import MagicMock
from katas.do_n_times import do_n_times

class TestDoNTimes(unittest.TestCase):

    def test_do_n_times_calls_target_correctly(self):
        mock_func = MagicMock()
        do_n_times(mock_func, 3)
        self.assertEqual(mock_func.call_count, 3)
    
    def test_do_n_times_calls_target_correctly(self):
        mock_func = MagicMock()
        do_n_times(mock_func, 3)
        self.assertEqual(mock_func.call_count, 3)
        
    def test_do_n_times_calls_target_with_zero(self):
        mock_func = MagicMock()
        do_n_times(mock_func, 0)
        self.assertEqual(mock_func.call_count, 0)
    
    def test_do_n_times_calls_target_with_negative(self):
        mock_func = MagicMock()
        do_n_times(mock_func, -5)
        self.assertEqual(mock_func.call_count, 0)

    def test_do_n_times_zero_calls(self):
        mock_func = MagicMock()
        do_n_times(mock_func, 0)
        self.assertEqual(mock_func.call_count, 0)

if __name__ == '__main__':
    unittest.main()
