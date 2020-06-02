# 151. Reverse Words in a String (Medium)

# Given an input string, reverse the string word by word.


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])
            
