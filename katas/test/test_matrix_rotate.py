import unittest
from katas.matrix_rotate import rotate_matrix


class TestMatrixRotate(unittest.TestCase):
    def rotate_matrix(self):
        matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

        res = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
        ]
        value = rotate_matrix(matrix)
        self.assertEqual(res, value)
