# Consider a function rev which reverses the digits in an integer. Here are some examples:

# rev(103) = 301
# rev(2400) = 42
# rev(9) = 9
# Given an array of non-negative integers arr, your task is to count the number of pairs (i, j) such that i ≤ j and arr[i] + rev(arr[j]) = arr[j] + rev(arr[i]).

# Example

# For arr = [1, 20, 2, 11], the output should be oppositeSums(arr) = 7.

# For (i, j) = (0, 0) equality holds: 1 + 1 = 1 + 1,
# For (i, j) = (0, 1) equality doesn't hold: 1 + 2 ≠ 20 + 1,
# For (i, j) = (0, 2) equality holds: 1 + 2 = 2 + 1,
# For (i, j) = (0, 3) equality holds: 1 + 11 = 11 + 1,
# For (i, j) = (1, 1) equality holds: 20 + 2 = 20 + 2,
# For (i, j) = (1, 2) equality doesn't hold: 20 + 2 ≠ 2 + 2,
# For (i, j) = (1, 3) equality doesn't hold: 20 + 11 ≠ 11 + 2,
# For (i, j) = (2, 2) equality holds: 2 + 2 = 2 + 2,
# For (i, j) = (2, 3) equality holds: 2 + 11 = 11 + 2,
# For (i, j) = (3, 3) equality holds: 11 + 11 = 11 + 11,
# So the total number of such pairs is 7.

# For arr = [32, 332, 100], the output should be oppositeSums(arr) = 4.

# For (i, j) = (0, 0) equality holds: 32 + 23 = 32 + 23,
# For (i, j) = (0, 1) equality doesn't hold: 32 + 233 ≠ 332 + 23,
# For (i, j) = (0, 2) equality doesn't hold: 32 + 1 ≠ 100 + 23,
# For (i, j) = (1, 1) equality holds: 332 + 233 = 332 + 233,
# For (i, j) = (1, 2) equality holds: 332 + 1 = 100 + 233,
# For (i, j) = (2, 2) equality holds: 100 + 1 = 100 + 1,
# So the total number of such pairs is 4.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer arr

# An array of non-negative integers.

# Guaranteed constraints:
# 2 ≤ arr.length ≤ 105,
# 0 ≤ arr[i] ≤ 109.

# [output] integer64

# The number of pairs (i, j) for which arr[i] + rev(arr[j]) = arr[j] + rev(arr[i]).


def oppositeSums(arr):
    d = {}
    ans = 0
    for i in arr:
        if i - rev(i) not in d:
            d[i-rev(i)] = 1
        else:
            d[i-rev(i)] += 1
    for k,v in d.items():
        ans += (v+1)*v/2
    return ans

def rev(n):
    s = str(n)
    return int(s[::-1])