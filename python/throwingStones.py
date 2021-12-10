# This question is asked by Amazon.
# You are given a group of stones, all of which have a positive weight.
# At each turn, we select the heaviest two stones and smash them together.
# When smashing these two stones together, one of two things can happen:
# If the stones are both the same weight, both stones are destroyed
# If the weights of the stones are not equal, the smaller of the two stones
# is destroyed and the remaining stone’s weight is updated to the difference
# (i.e. if we smash two stones together of weight 3 and weight 5 the stone with
# weight 3 is destroyed and the stone with original weight 5 now has weight 2).
# Continue smashing stones together until there is at most one stone left and
# return the weight of the remaining stone. If not stones remain, return zero.

# Ex: Given the following stones…

# stones = [2, 4, 3, 8], return 1
# 8 and 4 are smashed together, 4 is destroyed, 8 becomes 4.
# 4 and 3 are smashed together, 3 is destroyed, 4 becomes 1.
# 2 and 1 are smashed together, 1 is destroyed, 2 becomes 1.
# 1 is the last stone remaining and is therefore returned.

# Ex: Given the following stones…

# stones = [1, 2, 3, 4], return 0
# 4 and 3 are smashed together, 3 is destroyed, 4 becomes 1.
# 2 and 1 are smashed together, 1 is destroyed, 2 becomes 1.
# 1 and 1 are smashed together and both stones are destroyed.
# 0 is returned as no stones remain.


def throwingStones(stones):
    while len(stones) > 1:
        stones.sort()
        if stones[-1] > stones[-2]:
            stones[-1] -= stones[-2]
            stones[-2] = 0
        else:
            stones[-2] -= stones[-1]
            stones[-1] = 0
        stones = [x for x in stones if x != 0]
    if len(stones) == 0:
        return 0
    return stones[0]


# Recursive solution
def throwingStonesRecursive(stones):
    if len(stones) == 0:
        return 0
    if len(stones) == 1:
        return stones[0]
    stones.sort()
    if stones[-1] > stones[-2]:
        stones[-1] -= stones[-2]
        stones[-2] = 0
    else:
        stones[-2] -= stones[-1]
        stones[-1] = 0
    stones = [x for x in stones if x != 0]
    return throwingStonesRecursive(stones)


# Test cases
print("Iterative solution")
print(throwingStones([8, 4, 1]))
print(throwingStones([1, 2, 3, 10]))
print(throwingStones([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 22]))
print("\nRecursive solution")
print(throwingStonesRecursive([8, 4, 1]))
print(throwingStonesRecursive([1, 2, 3, 10]))
print(throwingStonesRecursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 22]))
