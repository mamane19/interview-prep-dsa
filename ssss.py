# Hello
# hi 

# For a given array which can contain duplicates, and a given number, write a method which 
# returns the index/indices (position/s) of the given number in the array, as if the input array was sorted.
# Input: [33, 22, 33, 11, 22]   22
#    [11, 22, 22, 33, 33] (how it would look like if it was sorted)
# Output: [1, 2] (zero-based indices)


# Solution:
# 1. Sort the array
# 2. Iterate through the array, and check if the number is equal to the current element.
# 3. If it is, return the index of the current element
# 4. If it is not, check if the current element is greater than the number. If it is, then we need to check the next element.
#    If it is not, then we need to check the previous element.
# 5. If the current element is greater than the number, then we need to check the previous element.
#    If the current element is not greater than the number, then we need to check the next element.

def find_index(arr, num):
    arr.sort()
    res = []
    for i in range(len(arr)):
        if arr[i] == num:
            res.append(i)
    return res


if __name__ == '__main__':
    print(find_index([33, 22, 33, 22, 22], 22))
      

# What if the number is not provided? Return the indices of the element which appears the most times 
# in the array as if in the sorted array.

# Input: [33, 44, 33, 11, 22]
# seen = {}




# Output: [2, 3]



'''
We have a function that we do not want to get called too frequently because it's very expensive.
Write a class RateLimit with an apply function that will call this function,
but no more than once every n milliseconds.
For Example:

r = RateLimit(f, 500)
r.apply()
r.apply() # fails because it happens within 500ms

time.sleep(3)
r.apply() # works ok
'''