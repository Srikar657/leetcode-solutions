class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=1
        while n>=r:
            n-=r
            r+=1
        return r-1
