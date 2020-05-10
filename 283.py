# 283. Move Zeroes (Easy)

# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.

# Note:
#  You must do this in-place without making a copy of the array.
#  Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZeroAt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonZeroAt] = nums[i]
                nonZeroAt += 1
        for i in range(nonZeroAt, len(nums)):
            nums[i] = 0
