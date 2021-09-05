
# O(w*h) time, O(1) space where w and h are the width and height of the matrix
def get_int_with_4_seq_values(matrix: list):
    row_len = len(matrix[0])
    col_len = len(matrix)

    # Check in rows
    for row in matrix:
        for i in range(len(row) - 3):
            if row[i] == 0:
                continue
            if row[i] == row[i + 1] == row[i + 2] == row[i + 3]:
                return row[i]

    # Check in columns
    for col in range(row_len):
        for i in range(col_len - 3):
            if matrix[i][col] == 0:
                continue
            if matrix[i][col] == matrix[i+1][col] == matrix[i+2][col] == matrix[i+3][col]:
                return matrix[i][col]

    # Check in diagonals (from top left to bottom right)
    for i in range(row_len - 3):
        for j in range(col_len - 3):
            if matrix[j][i] == 0:
                continue
            if matrix[j][i] == matrix[j+1][i+1] == matrix[j+2][i+2] == matrix[j+3][i+3]:
                return matrix[j][i]

    # Check in diagonals (top right to bottom left)
    for i in range(row_len - 3):
        for j in range(3, col_len):
            if matrix[j][i] == 0:
                continue
            if matrix[j][i] == matrix[j-1][i+1] == matrix[j-2][i+2] == matrix[j-3][i+3]:
                return matrix[j][i]

    return -1


if __name__ == '__main__':
    matrix = [
        [1, 2, 6, 0, 1, 1], 
        [7, 1, 1, 1, 1, 9], 
        [1, 7, 1, 0, 9, 0],
        [1, 6, 0, 9, 4, 6],
        [0, 0, 0, 0, 9, 0]]

    print(get_int_with_4_seq_values(matrix))



