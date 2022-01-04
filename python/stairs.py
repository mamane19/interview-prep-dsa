# This question is asked by Google.
# Given a staircase with N steps and the ability to climb either one or two steps at a time,
# return the total number of ways to arrive at the top of the staircase.

# Ex: Given the following value of N…
# N = 2, return 2
# 1 step + 1 step
# 2 steps

# Ex: Given the following value of N…
# N = 3, return 3
# 1 step + 1 step + 1 step
# 1 step + 2 steps
# 2 steps + 1 step


def count_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_ways(n-1) + count_ways(n-2)
