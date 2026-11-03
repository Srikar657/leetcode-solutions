class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        n=max(nums)
        for i in nums:
            res+=n-i
        return res
