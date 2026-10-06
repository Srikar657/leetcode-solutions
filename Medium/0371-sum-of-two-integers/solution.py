class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask=0xFFFFFFFF
        while b!=0:
            carry = (a&b)&mask
            a=(a^b)&mask
            b=(carry<<1)&mask
        if a > 0x7FFFFFFF:
            ans= ~(a^mask)
        else:
            ans=a
        return ans
