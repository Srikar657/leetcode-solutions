class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs=sorted(costs)
        count=0
        sums=0
        if min(costs)>coins:
            return 0
        for i in range(len(costs)):
            sums+=costs[i]
            if sums <= coins:
                count+=1
        return count
