class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[]
        while n>0:
            a.append(n%10)
            n//=10
        a.sort()
        if len(a)<2:
            return 0
        return a[-1]*a[-2]
