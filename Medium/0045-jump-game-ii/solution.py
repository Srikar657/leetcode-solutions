class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        maxs=0
        c=0
        for i in range(len(nums)-1):
            maxs=max(maxs,i+nums[i])
            if i == res:
                c+=1
                res=maxs
        return c
