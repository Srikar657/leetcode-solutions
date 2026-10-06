class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        counts = Counter(s)
        res = 0
        odd_found = False
        
        for c in counts.values():
            if c % 2 == 0:
                res += c
            else:
                res += c - 1
                odd_found = True
        
        if odd_found:
            res += 1
        return res
