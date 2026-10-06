class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix=nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                prefix+=nums[i]
            else:
                break
        num=set(nums)
        x=prefix
        while x in num:
            x+=1
        return x
