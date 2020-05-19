# 136. Single Number

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Solution 1: Hash Table
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for num in d:
            if d[num] == 1: 
              return num

# Solution 2: Bit Operation
class Solution:     
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
