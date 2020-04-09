# 392. Is Subsequence

# Given a string s and a string t, check if s is subsequence of t.

# You may assume that there is only lower case English letters in both s and t. 
# t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

# A subsequence of a string is a new string which is formed from the original string 
# by deleting some (can be none) of the characters without disturbing the relative positions 
# of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

# Solution1:

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pos, t_pos = 0, 0   
        ls, lt = len(s), len(t)
        
        if s == t or ls == 0:
            return True
        
        if ls > lt: 
            return False
        
        ch = s[s_pos]
        c = 0
        while t_pos < lt:
            if t[t_pos] == ch:
                c += 1
                if c == ls:
                    return True
                s_pos += 1
                ch = s[s_pos]
            t_pos+=1   
        return False
        
 
            
