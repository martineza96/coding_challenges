def search_matrix(matrix, x):
    """
    Searches for a value x in a row-wise and column-wise sorted matrix.

    Parameters:
    matrix (list of lists): 2D matrix where each row and column is sorted in increasing order.
    x (int): The value to search for.

    Returns:
    bool: True if x is found in the matrix, False otherwise.
    """
    # Implement the search logic here

    # Brute force approach

    # for row in matrix:
    #     for i in row:
    #         if x < i:
    #             break
    #         elif x == i:
    #             return True
    # return False

    # Optimized approach

    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0]) # For every element in one row will count the number of columns

    # Top right corner

    # First row of the matrix
    row = 0

    # Last index is len(cols) - 1 for 0 index in python
    col = cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == x:
            return True # Found the element
        elif matrix[row][col] > x:
            col -= 1 # Move left if the element is too large
        else:
            row += 1

    return False # Element not found


if __name__ == "__main__":
    # Example test cases
    test_cases = [
        (62, [[3, 30, 38],
              [20, 52, 54],
              [35, 60, 69]]),  # Expected output: False
        (55, [[18, 21, 27],
              [38, 55, 67]]),  # Expected output: True
        (35, [[3, 30, 38],
              [20, 52, 54],
              [35, 60, 69]])   # Expected output: True
    ]

    for i, (x, matrix) in enumerate(test_cases):
        print(f"Test Case {i+1}:")
        print(f"Matrix: {matrix}")
        print(f"Search for: {x}")
        print(f"Result: {search_matrix(matrix, x)}")
        print("-" * 30)