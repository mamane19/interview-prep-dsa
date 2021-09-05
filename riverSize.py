# Given a 2D array, of potentially unequal height and width, containing only 0s and 1s.
# Each 0 represents a land, and each 1 represents part of of a river.
# A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonal)
# to each other.
# The number of adjacent 1s forms the river's size.
# Note that a river can twist. In other words, it does not have to be a straight verticle or horizontal line.
# It can be L-shaped, for example.
# Write a function that returns an array of the sizes of all rivers.
# Example:
# Input:
# matrix = [
#   [1,0,0,1,0],
#   [1,0,1,0,0],
#   [0,0,1,0,1],
#   [1,0,1,0,1],
#   [1,0,1,1,0],
# ]
# Output: [1,2,2,2,5]

# Recursive solution
def riverSize(matrix):
    # Edge cases
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []
    if len(matrix) == 1:
        return [1] if matrix[0][0] == 1 else []
    # We recursively traverse the matrix, and keep track of the number of 1s in each column and row.
    def riverSizeHelper(row, col):
        # If we're at the edge of the matrix, return 0.
        if not isValid(row, col):
            return 0

        if matrix[row][col] == 0:
            return 0
        # We have a 1, so we check if it is part of a river.
        matrix[row][col] = 0
        size = 1
        size += riverSizeHelper(row - 1, col) # Up
        size += riverSizeHelper(row + 1, col) # Down
        size += riverSizeHelper(row, col - 1) # Left
        size += riverSizeHelper(row, col + 1) # Right
        return size
    # We check if the matrix is valid.
    def isValid(row, col):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return False
        return True
    # Now we can get the sizes of the rivers.
    sizes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                sizes.append(riverSizeHelper(i, j))
    return sizes


if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]
    print(riverSize(matrix))

