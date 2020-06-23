# 69. Sqrt(x)

# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# Solution 1 (Template 2): 
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 2, x // 2
        while left < right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        return left - 1
            
# Solution 2 (Template 3): 
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 2, x // 2
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot      
        return right
