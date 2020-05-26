# 697. Degree of an Array (Easy)

# Given a non-empty array of non-negative integers nums, the degree of this array is defined 
# as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Note:
#  nums.length will be between 1 and 50,000.
#  nums[i] will be an integer between 0 and 49,999.

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        res = len(nums)
        for i, num in enumerate(nums):
            if num in d:
                d[num][0] += 1
                d[num][2] = i
            else:
                d[num] = [1, i, i]
        degree = max(d.values(), key = lambda x: x[0])[0]
        for v in d.values():
            if v[0] == degree:
                res = min(res, v[2]-v[1])
        return res + 1
