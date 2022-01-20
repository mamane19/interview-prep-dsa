# given a list of numbers, find the missing numbers in the list and return them in a list


def find_missing_numbers(nums):
    return list(set(range(min(nums), max(nums) + 1)) - set(nums))


nums = [1, 4, 2, 0, 6, 8]
print(find_missing_numbers(nums))
