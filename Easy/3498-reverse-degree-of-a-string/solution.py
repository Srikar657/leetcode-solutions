class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        for i in range(len(s)):
            res+=(123 - ord(s[i]))*(i+1)
        return res
        
