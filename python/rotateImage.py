# # Given a 2D matrix, rotate the image by 90 degrees (clockwise).
# # 
# # Example:
# # [
# # [1,2,3],
# # [4,5,6],
# # [7,8,9]] 
# # -> [
# # [7,4,1],
# # [8,5,2],
# # [9,6,3]]
# # e.g2:
# # [
# # [ 5, 1, 9,11],
# # [ 2, 4, 8,10],
# # [13, 3, 6, 7],
# # [15,14,12,16]
# # ]
# # -> [
# # [15,13, 2, 5],
# # [14, 3, 4, 1],
# # [12, 6, 8, 9],
# # [16, 7,10,11]
# # ]

# # * Solution 1:
# # Brute force:
# def rotateImage(matrix):
#     n = len(matrix)
#     for i in range(n):
#         for j in range(i+1, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#     for i in range(n):
#         matrix[i].reverse()
#     return matrix


# You are given three statements.
# 1. Every bird that flies is green.
# 2. No weedle is green.
# 3. Some weedles are birds.
# Assuming that all the above are true, what else must be true?:
# 1. No weedle flies.
# 2. All weedles are birds.
# 3. No flying birds are weedles.
# 4. All weedles are blue.

# Answer: 
