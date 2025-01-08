# maximum_sum_subarray.py

def max_subarray_sum(arr):
    """
    Finds the maximum sum of a subarray using a specific algorithm.

    Parameters:
    arr (list): List of integers.

    Returns:
    int: Maximum sum of any subarray.
    """

    max_sum = float('-inf') #smallest possible value
    current_sum = 0 # start with an empty subarray

    for num in arr:
        current_sum = max(num, current_sum + num) #Grow or reset
        max_sum = max(max_sum, current_sum) #Update mac sum if needed

    return max_sum


if __name__ == "__main__":
    # Example test cases
    test_cases = [
        ([2, 3, -8, 7, -1, 2, 3], 11),  # Add expected output for reference
        ([-2, -4], -2),
        ([5, 4, 1, 7, 8], 25)
    ]

    for i, (arr, expected) in enumerate(test_cases):
        result = max_subarray_sum(arr)
        print(f"Test Case {i+1}:")
        print(f"Input: {arr}")
        print(f"Expected Output: {expected}")
        print(f"Your Output: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 30)
