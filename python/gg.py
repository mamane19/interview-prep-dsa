
# You're given a matrix of integers. 0 represents an empty espace.  
# Determine if there are any integers that have at least 4 sequential values across the rows, columns, and diagonals. 
# If there is Return the number.
# Sample Input1:
# [[0 1 3 2 1]
# [0 3 2 4 1]
# [1 1 1 1 0]]

# Sample Output1: 1

# Sample Input2:
# [[5 1 0 3 2]
# [0 5 2 4 1]
# [1 3 5 1 0]
# [2 2 1 5 0]]

# Sample Output2: 5

# Sample Input3:
# [[2 1 0 3 2]
# [2 1 2 4 1]
# [2 3 1 1 0]
# [2 1 1 0 1]
# [0 2 1 1 0]]

# Sample Output3: 2

def get_int_with_4_seq_values(matrix):
    # for i in range(3, row_len):
    #     for j in range(col_len - 3):
    #         if matrix[j][i] == 0:
    #             continue
    #         if matrix[j][i] == matrix[j+1][i-1] == matrix[j+2][i-2] == matrix[j+3][i-3]:
    #             return matrix[j][i]

    return 0

    
    


if __name__ == '__main__':
    matrix = [
        [4, 2, 0, 2, 4, 0], 
        [0, 4, 2, 4, 4, 2], 
        [1, 2, 4, 4, 0, 2],
        [2, 5, 4, 0, 1, 2],
        [0, 5, 0, 4, 0, 2]]
    print(get_int_with_4_seq_values(matrix))  
