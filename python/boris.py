# There is an integer array "nums" sorted in ascending order (with distinct values).

# Prior to being passed to your function, "nums" is rotated at 
# an unknown pivot index "k" (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-# indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
  
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
  
# Input: nums = [1], target = 0
# Output: -1


# O(log n) time and O(1) space
def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


if __name__ == '__main__':
    print(search([4,5,6,7,0,1,2], 1))
    print(search([4,5,6,7,0,1,2], 6))
    print(search([1], 1))
    print(search([1,3], 3))
