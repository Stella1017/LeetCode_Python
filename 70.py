# 70. Climbing Stairs

# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.

# Solution 1 Recursive: (could time out when n is large)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        else: return self.climbStairs(n-1) + self.climbStairs(n-2)

# Solution 2 Fibonacci Number
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        else: 
            res, a, b = 0, 1, 2
            for _ in range(n - 2):
                res = a + b
                a = b
                b = res
            return res
