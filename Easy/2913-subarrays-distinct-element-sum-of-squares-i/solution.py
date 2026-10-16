class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for i in range(len(nums)):
            r=set()
            for j in range(i,len(nums)):
                r.add(nums[j])
                res+=len(r)*len(r)
        return res
        
