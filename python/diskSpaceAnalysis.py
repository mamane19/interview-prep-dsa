# A company is performing an analysis on the computers at its main office.
# The computers are spaced along a single row. For each group of contiguous computers
# of a certain length,that is, for each segment, determine the minimum amount of disk space available on a computer.
# Return the maximum of these values as your answer.

# Example:
# Input:
# n = 4, the number of computers
# space = [8, 2, 4, 6]
# x = 2, the segment length
# The free disk space of computers in each of the segments is as follows:
# [8,2], [2,4], [4,6]. The minima of the three segments are [2,2,4]. the maximum of these values is 4.


from collections import deque


def findMax(x, space):
    n = len(space)
    if n * x == 0:
        return []
    if x > n:
        return []

    deq = deque()
    res = []
    i = 0
    while i < n:
        if deq and deq[0] == i - x:
            deq.popleft()
        while deq and space[deq[-1]] > space[i]:
            deq.pop()
        deq.append(i)

        if i >= x - 1:
            res.append(space[deq[0]])
        i += 1
    print(res)
    print(max(res))
