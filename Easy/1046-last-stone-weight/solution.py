class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            val1 = -heapq.heappop(stones)
            val2 = -heapq.heappop(stones)
            if val1 == val2:
                continue
            else:
                v=abs(val1-val2)
                heapq.heappush(stones,-v)
        return -stones[0] if stones else 0
