# This question is asked by Google. 
# Given two strings, s and t, return the length of their longest subsequence.

# Ex: Given the following strings s and t…

# s = "xyz", t = "xyz". return 3.
# Ex: Given the following strings s and t…

# s = "abca", t = "acea", return 3.
# Ex: Given the following strings s and t…

# s = "abc", t = "def", return 0.


def longestCommonSubsequence(s, t):
     # Write your code here
     if not s or not t:
          return 0
     dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
     for i in range(1, len(s) + 1):
          for j in range(1, len(t) + 1):
               if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
               else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
     return dp[-1][-1]


s = "abca"
t = "acea"
print(longestCommonSubsequence(s, t))

s = "xyz"
t = "xyz"
print(longestCommonSubsequence(s, t))

s = "abc"
t = "def"
print(longestCommonSubsequence(s, t))