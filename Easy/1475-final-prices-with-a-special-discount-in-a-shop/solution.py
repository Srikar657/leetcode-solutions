class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n=len(prices)
        res=[]
        for i in range(n):
            l=0
            for j in range(i+1,n):
                if prices[j]<=prices[i]:
                    res.append(prices[i]-prices[j])
                    l=1
                    break
            if l == 0:
                res.append(prices[i])
        return res
