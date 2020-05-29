# 448. Find All Numbers Disappeared in an Array (Easy)

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Brute Force
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        s = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in s:
                res.append(i)         
        return res
        
# Space O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
            for i in range(len(nums)):
                new_idx = abs(nums[i]) - 1
                if nums[new_idx] > 0:
                    nums[new_idx] *= -1
            res = []
            for i in range(1, len(nums) + 1):
                if nums[i - 1] > 0:
                    res.append(i)
            
            return res
