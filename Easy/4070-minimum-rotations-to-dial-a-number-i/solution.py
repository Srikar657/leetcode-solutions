class Solution(object):
    def minRotations(self, s):
        """
        :type s: str
        :rtype: int
        """
        t=0
        c=0
        for i in s:
            k=abs(c-int(i))
            t+=min(k,10-k)
            c=int(i)
        return t
