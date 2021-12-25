# This question is asked by Facebook. 
# Given an array of unsorted integers, return the length of its longest increasing subsequence.
# Note: You may assume the array will only contain positive numbers.

# Ex: Given the following array nums…

# nums = [1, 9, 7, 4, 7, 13], return 4.
# The longest increasing subsequence is 1, 4, 7, 13.


def longestIncreasingSubsequence(nums):
     # Write your code here
     if not nums:
          return 0
     dp = [1] * len(nums)
     for i in range(1, len(nums)):
          for j in range(i):
               if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
     return max(dp)


nums = [1, 9, 7, 4, 7, 13]
print(longestIncreasingSubsequence(nums))