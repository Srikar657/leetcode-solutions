class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            prob=1
            for d in str(n):
                prob*=int(d)
            if prob%t==0:
                return n
            n+=1
