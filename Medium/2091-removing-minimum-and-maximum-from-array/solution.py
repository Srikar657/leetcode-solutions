class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nn=len(nums)
        maxs=nums.index(max(nums))
        mins=nums.index(min(nums))
        if mins>maxs:
            mins,maxs=maxs,mins
        s1=maxs+1
        s2=nn-mins
        s3=(mins+1)+(nn-maxs)
        return min(s1,s2,s3)
