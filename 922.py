# 922. Sort Array By Parity II (Easy)

# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

# You may return any answer array that satisfies this condition.

# Note:
#  2 <= A.length <= 20000
#  A.length % 2 == 0
#  0 <= A[i] <= 1000

# Solution 1: Two pointers:
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i, j = 0, 1
        while i < len(A) and j < len(A):
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]
            if A[i] % 2 == 0:
                i += 2
            if A[j] % 2 == 1:
                j += 2
        return A

# Solution 2: 
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
