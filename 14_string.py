# 14. Longest Common Prefix (Easy)

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""

# Explanation: There is no common prefix among the input strings.

# Note:
# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        for x in zip(*strs):
            if len(set(x)) == 1:
                res.append(x[0])
            else:
                break
        return "".join(res)
