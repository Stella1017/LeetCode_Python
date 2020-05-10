# 905. Sort Array By Parity (Easy)

# Given an array A of non-negative integers, return an array consisting 
# of all the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

# Note:

#  1 <= A.length <= 5000
#  0 <= A[i] <= 5000

# Solution 1. Two pointers:
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        lo, hi = 0, len(A) - 1
        while lo < hi:
            if A[lo] % 2 == 1 and A[hi] % 2 == 0: # if A[lo] % 2 > A[hi] % 2:
                A[lo], A[hi] = A[hi], A[lo]
            if A[lo] % 2 == 0:
                lo += 1
            if A[hi] % 2 == 1:
                hi -= 1
        return A

# Solution 2. Two Pass:
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
    return([x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1])
