# 1266. Minimum Time Visiting All Points (Easy)

# On a plane there are n points with integer coordinates points[i] = [xi, yi]. 
# Your task is to find the minimum time in seconds to visit all points.

# You can move according to the next rules:

# In one second always you can either move vertically, horizontally by one unit or diagonally 
# (it means to move one unit vertically and one unit horizontally in one second).
# You have to visit the points in the same order as they appear in the array.

# Constraints:

# points.length == n
# 1 <= n <= 100
# points[i].length == 2
# -1000 <= points[i][0], points[i][1] <= 1000

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for p, q in zip(points[:-1], points[1:]):
            res += max(abs(p[0]-q[0]), abs(p[1]-q[1]))
        return res
 
