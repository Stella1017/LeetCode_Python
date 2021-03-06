# 867. Transpose Matrix

# Given a matrix A, return the transpose of A.

# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

# Solution 1: list comprehension
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
        
# Solution 2:
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(A[0])):
            temp = []
            for j in range(len(A)):
                temp.append(A[j][i])
            res.append(temp)
        return res
