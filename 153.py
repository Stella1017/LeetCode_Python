# 153. Find Minimum in Rotated Sorted Array Medium

# Suppose an array sorted in ascending order is rotated 
# at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# You may assume no duplicate exists in the array.

# Solution1: Binary Search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                left = mid + 1
            else: 
                right = mid 
