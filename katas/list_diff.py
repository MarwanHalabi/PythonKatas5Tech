from typing import List

def find_difference(numbers: List):
    """
    Finds the difference between the largest and smallest numbers in the list.

    Args:
        numbers: the list of integers

    Returns:
        the difference between the largest and smallest numbers
    """
    mx = max(numbers) if numbers else 0
    mn = min(numbers) if numbers else 0
    
    if mx * mn < 0:
        return abs(mn) + abs(mx)
    return mx - mn


if __name__ == '__main__':
    sample_list = [10, 3, 5, 6, 20, -2]
    difference = find_difference(sample_list)
    print(difference)  # 22 should be printed