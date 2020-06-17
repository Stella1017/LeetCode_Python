# 20. Valid Parentheses

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
#  Open brackets must be closed by the same type of brackets.
#  Open brackets must be closed in the correct order.
  
# Note that an empty string is also considered valid.

class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', '}':'{', ']':'['}
        res = []       
        if len(s) % 2 != 0: 
            return False
        for char in s:
            if char in d:
                last_element = res.pop() if res else '#'
                if d[char] != last_element:
                    return False
            else:
                res.append(char)
        return not res # len(res) == 0
