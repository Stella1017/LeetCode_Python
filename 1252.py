# 1252. Cells with Odd Values in a Matrix (Easy)

# Given n and m which are the dimensions of a matrix initialized by zeros and given 
# an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have 
# to increment all cells in row ri and column ci by 1.

# Return the number of cells with odd values in the matrix after applying the increment to all indices.

# Constraints:

#  1 <= n <= 50
#  1 <= m <= 50
#  1 <= indices.length <= 100
#  0 <= indices[i][0] < n
#  0 <= indices[i][1] < m

# Solution: Bit Operation
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        res = [0] * n * m
        for indice in indices:
            for j in range(m):
                res[indice[0] * m + j] ^= 1
                # print(res)
            for i in range(n):
                res[indice[1] + m * i] ^= 1
                # print(res)
        return sum(res)
