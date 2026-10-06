class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        t=str(n)
        sums=0
        r=""
        for i in t:
            if i!='0':
                r+=(i)
                sums+=int(i)
        if not r:
            return 0
        return int(r)*sums
