class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        nums.sort()
        res=[]
        for i in range(1,len(nums)):
            res.append(nums[i]-nums[i-1])
        return max(res)
