# 442. Find All Duplicates in an Array (Medium)

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Hash Table
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        res = [k for k,v in d.items() if v == 2]
        
        return res

# Advanced (by https://leetcode.com/user6547d/)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #1 <= a[i] <= n indicates the value of the any element has a position in the array
        #linear time indicates no sorting, extra space no hash
        res = []
        for ele in nums:
            if nums[abs(ele)-1] >0: #mark array position of the value
                nums[abs(ele)-1] *= -1
            else: #duplicates since both are marking the same position
                res.append(abs(ele)) 
        return res
