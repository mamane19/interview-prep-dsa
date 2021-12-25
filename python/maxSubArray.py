# This question is asked by Facebook. 
# Given an integer array, return the sum of its contiguous subarray that produces the largest value.
# Note: Your subarray must contain at least one value.

# Ex: Given the following integer arrays…

# nums = [-3,8,-8,2], return 8 (8)
# nums = [2, 3,-4, 2], return 5 (2 + 3)
# nums = [1, 5,-2, -3, 7], return 8 (1 + 5 + (-2) + (-3) + 7)


def maxSubArray(nums):
     # Write your code here
     if not nums:
          return 0
     dp = [0] * len(nums)
     dp[0] = nums[0]
     for i in range(1, len(nums)):
          dp[i] = max(dp[i - 1] + nums[i], nums[i])
     return max(dp) 