# the cartesian product of two lists of numbers A and B is defined to be the set 
# of all points (a, b) where a in A and b in B. It is a generalization of the 
# Cartesian product of the sets A and B. It is usually denoted as A x B, and is 
# called the cartesian product since it originated in Descartes' formulation of
# analytic geometry.

# Given two sets of real numbers, their cartesian product comes in form of 
# ordered pairs. For example, if A = {1, 2, 3} and B = {4, 5, 6}, then the
# cartesian product of A and B is {(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6),
# (3, 4), (3, 5), (3, 6)}.

# Now given a coordiante tuples (i, j), where i indicates A(i) and j indicates
# B(j), with A, B known, implement a function that returns the index of a member
# in cartesian product C according to (i, j).
# For example:
# coordinate (1, 0): return index: 2
# coordinate (1, 1): return index: 4
# coordinate (2, 1): retunr index: 5

# The time complexity of the function should be O(1).

# Note: 
# 1. The cartesian product of two sets is not necessarily a set. For example,
# {1, 2, 3} x {4, 5, 6} = {(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4),
# (3, 5), (3, 6)}. However, the cartesian product of two sets is a set.
# 2. The cartesian product of two sets is not necessarily a set. For example,
# {1, 2, 3} x {4, 5, 6} = {(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4),
# (3, 5), (3, 6)}. However, the cartesian product of two sets is a set.

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#                                                                               *
#                                                   *
#                                                                               *
#                                                                               *
#                                                                               *
#                                                                               *

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# So, the idea is to use the same logic as the problem of finding the
# index of an element in a list.

# Solution:

def cartesian_product(A, B):
    return [(a, b) for a in A for b in B]

# Now, let's get the index of the element in the cartesian product.

# O(1) time complexity
def get_index(coordinate: tuple, cartesian_product):
    return cartesian_product.index(coordinate)

if __name__ == "__main__":
    A = [1, 2, 3]
    B = [4, 5, 6]
    print(cartesian_product(A, B))
    print(get_index((1, 6), cartesian_product(A, B)))
