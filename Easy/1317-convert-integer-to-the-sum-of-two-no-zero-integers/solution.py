class Solution(object):
    import random
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(n):
            if ((i+(n-i))==n and '0' not in str(i) and '0' not in str(n-i)):
                return [i,n-i]
