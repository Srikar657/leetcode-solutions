class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        sums=0
        for i in nums:
            sums+=i
            res.append(sums)
        return res
