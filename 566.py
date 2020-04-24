# 566. Reshape the Matrix

# In MATLAB, there is a very useful function called 'reshape', 
# which can reshape a matrix into a new one with different size but keep its original data.

# You're given a matrix represented by a two-dimensional array, and two positive integers r and c 
# representing the row number and column number of the wanted reshaped matrix, respectively.

# The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the 'reshape' operation with given parameters is possible and legal, 
# output the new reshaped matrix; Otherwise, output the original matrix.

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        numlist = [num for row in nums for num in row]
        res = []
        if len(numlist) / r == c:
            for i in range(r):
                row = numlist[i * c : (i + 1) * c]
                res.append(row)
            return res
        return nums
