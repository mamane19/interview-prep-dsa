# You are given an array of non-negative integers numbers. You are allowed to choose any number from this array and swap any two digits in it. If after the swap operation the number contains leading zeros, they can be omitted and not considered (eg: 010 will be considered just 10).

# Your task is to check whether it is possible to apply the swap operation at most once, so that the elements of the resulting array are strictly increasing.

# Example

# For numbers = [1, 5, 10, 20], the output should be makeIncreasing(numbers) = true.

# The initial array is already strictly increasing, so no actions are required.

# For numbers = [1, 3, 900, 10], the output should be makeIncreasing(numbers) = true.

# By choosing numbers[2] = 900 and swapping its first and third digits, the resulting number 009 is considered to be just 9. So the updated array will look like [1, 3, 9, 10], which is strictly increasing.

# For numbers = [13, 31, 30], the output should be makeIncreasing(numbers) = false.

# The initial array elements are not increasing.
# By swapping the digits of numbers[0] = 13, the array becomes [31, 31, 30] which is not strictly increasing;
# By swapping the digits of numbers[1] = 31, the array becomes [13, 13, 30] which is not strictly increasing;
# By swapping the digits of numbers[2] = 30, the array becomes [13, 31, 3] which is not strictly increasing;
# So, it's not possible to obtain a strictly increasing array, and the answer is false.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer numbers

# An array of non-negative integers.

# Guaranteed constraints:
# 1 ≤ numbers.length ≤ 103,
# 0 ≤ numbers[i] ≤ 103.

# [output] boolean

# Return true if it is possible to obtain a strictly increasing array by applying the digit-swap operation at most once, and false otherwise.


def makeIncreasing(numbers):
    if len(numbers) <= 1:
        return True
    else:
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1] and isSwapPossible(numbers[i], numbers[i+1]) == False:
                return False
        return True


def isSwapPossible(a, b):
    if a == b:
        return True
    else:
        if a > b:
            return False
        else:
            return True

if __name__ == "__main__":
    print(makeIncreasing([1, 5, 10, 20]))
    print(makeIncreasing([1, 3, 900, 10]))
    print(makeIncreasing([13, 31, 30]))
