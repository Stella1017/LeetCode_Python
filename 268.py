# 268. Missing Number

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
# find the one that is missing from the array.

# Solution 1: HashSet
class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

# Solution 2: Math
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = len(nums) * (len(nums)+1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Solution 3: Bit Operation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
