class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        c=str(x)
        c=c[::-1]
        if x<0:
            c=c[:-1]
        if int(c)>-2**31 and int(c)<2**31:
            if x<0:
                c = "-"+c
                return int(c)
            return int(c)
        return 0
        
