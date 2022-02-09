# Design and implement an algorithm that takes: a list containing n distinct natural numbers
# and a number k ≤ n and calculates the sum of the k largest numbers in the array.
# For example, if the list is {3, 7, 5, 12, 6} and k = 3, then the algorithm should return 25= (12+7+6).


#!/usr/bin/env python3


def sumOfKLargestDiff(arr, k):
    if not arr or k < 1 or k > len(arr):
        return None
    arr.sort()

    return sum(arr[-k:])


if __name__ == "__main__":
    print(sumOfKLargestDiff([3, 7, 5, 12, 6], 3))
