# 977. Squares of a Sorted Array (Easy)

# Given an array of integers A sorted in non-decreasing order, return an array of 
# the squares of each number, also in sorted non-decreasing order.

# Note:
#  1 <= A.length <= 10000
#  -10000 <= A[i] <= 10000
#  A is sorted in non-decreasing order.

# Two pointers:
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        lo, hi = 0, len(A) - 1
        res = []
        while lo <= hi:
            if abs(A[lo]) < abs(A[hi]):
                res.append(A[hi]**2)
                hi -= 1
            else: 
                res.append(A[lo]**2)
                lo += 1
        return res[::-1]
