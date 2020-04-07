# 561. Array Partition I

# Given an array of 2n integers, your task is to group these integers into n pairs
# of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) 
# for all i from 1 to n as large as possible.


# Solution1:
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        res = 0
        for i,num in enumerate(nums):
            if i % 2 == 0:
                res += num
        
        return res
