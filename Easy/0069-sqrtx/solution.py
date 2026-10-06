class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x
        low=2
        high=x//2
        ans=1
        while low<=high:
            mid=(low+high)//2
            square=mid*mid
            if square==x:
                return mid
            elif square<x:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
