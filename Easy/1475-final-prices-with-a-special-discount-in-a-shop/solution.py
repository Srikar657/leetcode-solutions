class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        nums=prices
        n=len(prices)
        res=[]
        t=-1
        for i in range(n):
            while res and nums[res[t]]>=nums[i]:
                nums[res[t]]=nums[res[t]]-nums[i]
                res.pop()
            res.append(i)
        return nums
