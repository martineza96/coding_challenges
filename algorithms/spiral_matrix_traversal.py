mat = [[1,  2,  3,  4],
 [5,  6,  7,  8],
 [9,  10, 11, 12],
 [13, 14, 15, 16]]

def boundary_traversal(mat):
    top = 0
    bottom = len(mat) - 1
    left = 0
    right = len(mat[0]) - 1

    while top <= bottom and left <= right:
        # Traverse top row
        for i in range(left, right + 1):
            print(mat[top][i], end=" ")
        top += 1

        # Traverse rightmost column
        for i in range(top, bottom + 1):
            print(mat[i][right], end=" ")
        right -= 1

        # Traverse bottom row (if there is one)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                print(mat[bottom][i], end=" ")
            bottom -= 1

        # Traverse leftmost column (if there is one)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(mat[i][left], end=" ")
            left += 1

    return None

boundary_traversal(mat)