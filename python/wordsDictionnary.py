# This question is asked by Amazon. 
# Given a string s and a list of words representing a dictionary, 
# return whether or not the entirety of s can be segmented into dictionary words.
# Note: You may assume all characters in s and the dictionary are lowercase.

# Ex: Given the following string s and dictionary…

# s = "thedailybyte", dictionary = ["the", "daily", "byte"], return true.

# Ex: Given the following string s and dictionary…

# s = "pizzaplanet", dictionary = ["plane", "pizza"], return false.


def wordBreak(s, wordDict):
     # Write your code here
     if not s:
          return True
     if not wordDict:
          return False
     dp = [False] * (len(s) + 1)
     dp[0] = True
     for i in range(1, len(s) + 1):
          for j in range(i):
               if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
     return dp[-1]


s = "pizzaplanet"
wordDict = ["plane", "pizza"]
print(wordBreak(s, wordDict))

s = "thedailybyte"
wordDict = ["the", "daily", "byte"]
print(wordBreak(s, wordDict))
