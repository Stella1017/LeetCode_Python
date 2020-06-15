# 349. Intersection of Two Arrays

# Given two arrays, write a function to compute their intersection.

# Example:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]

# Note:
#  Each element in the result must be unique.
#  The result can be in any order.

# Solution 1 using set:
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        s1 = set(nums1)
        s2 = set(nums2)
        for i in s1:
            if i in s2: res.append(i)
        return res

# Solution 2 two pointers:
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        l, r = 0, 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] == nums2[r]:
                while l + 1 < len(nums1) and nums1[l] == nums1[l + 1]:
                    l += 1
                while r + 1 < len(nums2) and nums2[r] == nums2[r + 1]:
                    r += 1 
                res.append(nums1[l])
                l += 1
                r += 1
            elif nums1[l] > nums2[r]:
                r += 1
            else: 
                l += 1
        return res
