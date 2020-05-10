# 1099. Two Sum Less Than K (Easy)

# Given an array A of integers and integer K, return the maximum S such that 
# there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

# Note:
#   1 <= A.length <= 100
#   1 <= A[i] <= 1000
#   1 <= K <= 2000 

# Two pointers:
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        lo, hi = 0, len(A) - 1
        res = float('-inf')
        
        while lo < hi:
            if A[lo] + A[hi] >= K:
                hi -= 1
            else:
                res = max(res, A[lo] + A[hi])
                lo += 1
        
        return max(res, -1)
