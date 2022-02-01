# write a function that given an integer N(1 <= N <= 100), returns an array containing N unique integers
# such that the sum of the integers is 0. The function can return any such array.

#Example: N = 3
#Output: [-1, 0, 1]

#Example: N = 4
#Output: [1, 0, -3, 2] or [-2, 1, -4, 5]


#!/usr/bin/env python3

def sumToZero(n):
    if n < 1 or n > 100:
        return None

    # create an array of n unique integers
    arr = []
    for i in range(n):
        arr.append(i)

    # create a list of all possible combinations of the array
    combos = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            combos.append([arr[i], arr[j]])

    # find the combinations that sum to 0
    zero_combos = []
    for combo in combos:
        if sum(combo) == 0:
            zero_combos.append(combo)

    # return the first combination that sums to 0
    return zero_combos[0]


print(sumToZero(3))
print(sumToZero(4))
