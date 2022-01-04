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

# Ex: Given the following value of N…
# N = 4, return 5
# 1 step + 1 step + 1 step + 1 step
# 1 step + 1 step + 2 steps
# 1 step + 2 steps + 1 step
# 2 steps + 1 step + 1 step
# 2 steps + 2 steps


def count_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_ways(n-1) + count_ways(n-2)

# iterative solution


def count_ways_iter(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        ways = [0] * (n+1)
        ways[1] = 1
        ways[2] = 2
        for i in range(3, n+1):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n]


print(count_ways(2))
print(count_ways_iter(2))
print(count_ways(3))
print(count_ways_iter(3))
print(count_ways(4))
print(count_ways_iter(4))
print(count_ways(5))
print(count_ways_iter(5))
