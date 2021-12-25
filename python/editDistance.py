# This question is asked by Google. 
# Given two strings s and t, return the minimum number of operations 
# needed to convert s into t where a single operation consists of inserting 
# a character, deleting a character, or replacing a character.

# Ex: Given the following strings s and t…

# s = "cat", t = "bat", return 1.

# Ex: Given the following strings s and t…

# s = "beach", t = "batch", return 2.
# Delete the 'e' in "beach" and add a 't' to the resulting "bach".


def minDistance(s, t):
     # Write your code here
     if not s:
          return len(t)
     if not t:
          return len(s)
     dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
     for i in range(1, len(s) + 1):
          for j in range(1, len(t) + 1):
               if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
               else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
     return dp[-1][-1]


s = "beach"
t = "batch"
print(minDistance(s, t))

s = "cat"
t = "bat"
print(minDistance(s, t))