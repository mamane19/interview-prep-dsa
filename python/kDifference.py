# Given an array of distinct integers and a target value, determine the number of distinct pairs of integers
# in the array with an absolute difference equal to the target amount. Two pairs are distinct if they differ
# in at least one value. To illustrate, the pairs (1, 2), (2, 3), and (3, 4) are distinct, whereas (1, 2),

#######################################################################################################################

# First Solution
import collections


def kDifference(arr, k):
    c = collections.Counter(arr)
    count = 0
    for i in c:
        if i - k in c:
            count += c[i - k]
    return count


# Second Solution
def kDifference2(arr, k):
    c = collections.Counter(arr)
    count = 0
    for i in c:
        if k > 0 and i + k in c or k == 0 and c[i] > 1:
            count += 1
    return count


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    k = 10
    print(kDifference(arr, k))
    print(kDifference2(arr, k))
