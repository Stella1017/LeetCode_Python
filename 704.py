# Binary Search
# 704 Binary Search (Easy)

# Given a sorted (in ascending order) integer array nums of n elements and a target value, 
# write a function to search target in nums. If target exists, then return its index, otherwise return -1.

# Note:
#  You may assume that all elements in nums are unique.
#  n will be in the range [1, 10000].
#  The value of each element in nums will be in the range [-9999, 9999].

# Template 2:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else: 
                right = mid
        if nums[left] == target:
            return left
        else:
            return -1



# Template 3:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] ==  target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else: 
                left = mid + 1
        return -1
        
     