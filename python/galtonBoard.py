# This question is asked by Google. 
# A ball is dropped into a special Galton board where at each level 
# in the board the ball can only move right or down. Given that the Galton board 
# has M rows and N columns, return the total number of unique ways the ball can 
# arrive at the bottom right cell of the Galton board.

# Ex: Given the following values of M and N…

# M = 2, N = 2, return 2.
# The possible paths are DOWN -> RIGHT and RIGHT -> DOWN 
# Ex: Given the following values of M and N…

# M = 4, N = 3, return 10.


def uniquePaths(M, N):
     # Write your code here
     if M == 0 or N == 0:
          return 0
     dp = [[0] * N for _ in range(M)]
     for i in range(M):
          dp[i][0] = 1
     for j in range(N):
          dp[0][j] = 1
     for i in range(1, M):
          for j in range(1, N):
               dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
     return dp[-1][-1]