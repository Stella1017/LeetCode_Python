# 1295. Find Numbers with Even Number of Digits (Easy)

# Given an array nums of integers, return how many of them contain an even number of digits.

# Constraints:

# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^5

# Solution 1 (math):
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if floor(math.log10(num) % 2) == 1:
                res += 1
        return res
        
# Solution 2 (string):
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(num)) % 2 == 0 if num != 0 else 0 for num in nums)
