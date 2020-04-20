# 896. Monotonic Array

# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = dec = True
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                inc = False
            if A[i] < A[i+1]:
                dec = False
        return inc or dec
        
# Time: O(N)
# Space: O(1)
