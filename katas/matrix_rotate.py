def rotate_matrix(matrix):
    """
    Rotates the given square matrix 90 degrees clockwise in place.

    Args:
        matrix: the 2D square matrix to rotate
    """
    n = len(matrix)
    for cir in range(n//2):
        for i in range(cir, n - cir -1):
            start = [cir, i]
            cell_2 = [start[1], n - start[0] - 1]
            cell_3 = [cell_2[1], n - cell_2[0] - 1]
            cell_4 = [cell_3[1], n - cell_3[0]- 1]
            
            matrix[start[0]][start[1]], matrix[cell_2[0]][cell_2[1]], matrix[cell_3[0]][cell_3[1]], matrix[cell_4[0]][cell_4[1]] = matrix[cell_4[0]][cell_4[1]], matrix[start[0]][start[1]], matrix[cell_2[0]][cell_2[1]], matrix[cell_3[0]][cell_3[1]]


def print_matrix(matrix):
    """
    Helper function to print a 2D matrix.

    Args:
        matrix: the matrix to print
    """
    for row in matrix:
        print(' '.join(str(value) for value in row))


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    print_matrix(matrix)
    rotate_matrix(matrix)
    print("Matrix after 90-degree clockwise rotation:")
    print_matrix(matrix)

    # Expected output:
    # Original Matrix:
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # Matrix after 90-degree clockwise rotation:
    # 7 4 1
    # 8 5 2
    # 9 6 3