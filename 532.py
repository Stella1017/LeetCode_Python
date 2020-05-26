# 532. K-diff Pairs in an Array

# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
# Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and 
# their absolute difference is k.

# Solution 1: hash set
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # k is absolute diff, then should be non-negative
        if k < 0: 
            return 0
        
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1        
        res = 0
        for num, v in d.items():
            if (k==0 and v>1) or (k!=0 and num+k in d):
                res += 1
        return res

# Solution 2: two pointers
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        nums.sort()
        lo, hi = 0, 1
        res = set()
        while lo < len(nums) and hi < len(nums):
            if nums[lo] + k == nums[hi] and lo != hi:
                res.add((nums[lo], nums[hi]))
                hi += 1
            elif nums[lo] + k < nums[hi]:
                lo += 1
            else: 
                hi += 1
        return len(res)
