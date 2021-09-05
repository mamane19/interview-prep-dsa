# A covert agent has some crucial information stored in the form of an array of integers. 
# The array contains sensitive information and it must not be revealed to anyone. However, 
# there are few things about the array which are known.

# An array is said to be analogous to the secret array if all of the following conditions are true:
# - The length of the array is equal to the length of the secret array.
# - Each integer in the array lies in the interval [lowerBound, upperBound].
# - The difference between each pair of consecutive integers of the array must be equal to 
# the difference between the respective pair of consecutive integers in the secret array. 
# In other words, let the secret array be [s[0], s[1],...s[n-1]]
# and let the analogous array be [a[0], a[1],...a[n-1]], then (a[i-1] - a[i]) must be equal to
# (s[i-1] - s[i]) for each i from 1 to n-1.

# Given the value of the integers lowerBound and upperBound  inclusive, and the array of differences 
# between each pair of consecutive integers of the secret array, find the number of arrays that are 
# analogous to the secret array. If there is no array analogous to the secret array, return 0.

# For example:
# consecutiveDifferences = [-2, -1, -2, 5]
# lowerBound = 3
# upperBound = 10
# The logic to create an analogous array starting from the lower bound is:
# Start with value 3,
# Subtract consecutiveDistances[0], 3 - (-2) = 5,
# Subtract consecutiveDistances[1], 5 - (-1) = 6,
# Subtract consecutiveDistances[2], 6 - (-2) = 8
# Subtract consecutiveDistances[3], 8 - 5 = 3
# Note that none of the values is out of bounds. All possible analogous arrays are:
# [3, 5, 6, 8, 3]
# [4, 6, 7, 9, 4]
# [5, 7, 8, 10, 5]

# The answer is 3.


# Note:
# consecutiveDifferences.length == secretArray.length
# lowerBound <= consecutiveDifferences[i] <= upperBound
# consecutiveDifferences[i] - consecutiveDifferences[i-1] == secretArray[i] - secretArray[i-1] for all i.
# lowerBound <= secretArray[i] <= upperBound



















































































# def countAnalogousArrays(consecutiveDifference, lowerBound, upperBound):
#     maxDiff = float('-inf')
#     minDiff = float('inf')
#     count = 0
#     # edge cases
#     if len(consecutiveDifference) == 0:
#         return 0
#     if upperBound < lowerBound:
#         return 0
    
#     for diff in consecutiveDifference:
#         count += diff
#         if count > maxDiff:
#             maxDiff = count
#         if count < minDiff:
#             minDiff = count
#     maxValidUpperBound = upperBound + minDiff if upperBound + minDiff < upperBound else upperBound
#     minValidLowerBound = lowerBound + maxDiff if lowerBound + maxDiff > lowerBound else lowerBound
#     if maxValidUpperBound >= minValidLowerBound:
#         return (maxValidUpperBound - minValidLowerBound) + 1
#     else:
#         return 0