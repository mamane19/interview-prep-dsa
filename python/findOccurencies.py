# write an algorithm that takes as an input a list. Return true if the each of the elements of the list occurs an odd number of times.
# Otherwise, return false. the list can have duplicate elements.

# O(n) time and O(n) space
def oddOccurrences(arr):
    if not arr:
        return False

    seen = {}
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen[arr[i]] = 1
        else:
            seen[arr[i]] += 1

    for key in seen:
        if seen[key] % 2 == 0:
            return False
    return True


if __name__ == "__main__":
    print(oddOccurrences([1, 2, 2, 3, 5, 5, 5]))
    print(oddOccurrences([1, 2, 3, 2, 5, 2]))
    print(oddOccurrences([1, 2, 3, 2, 5, 2, 1]))
    print(oddOccurrences([1, 2, 3, 2, 5, 2, 1, 1]))
