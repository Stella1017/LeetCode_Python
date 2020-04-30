# 892. Surface Area of 3D Shapes

# On a N * N grid, we place some 1 * 1 * 1 cubes.

# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

# Return the total surface area of the resulting shapes.

# Note:
#  1 <= N <= 50
#  0 <= grid[i][j] <= 50

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]: 
                    res += (2 + grid[i][j] * 4)
                if j-1 >= 0:
                    res -= min(grid[i][j], grid[i][j-1]) * 2
                if i-1 >= 0:
                    res -= min(grid[i][j], grid[i-1][j]) * 2
        return res
      
Time: O(N^2)
Space: O(1)
