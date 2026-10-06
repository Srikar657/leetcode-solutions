class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        m=0
        for i in s:
            if i =="(":
                res+=1
            elif i==")":
                res-=1
            m=max(m,res)
        return m
