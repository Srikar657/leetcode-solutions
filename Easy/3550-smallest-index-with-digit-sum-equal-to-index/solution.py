class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            res=0
            x=nums[i]
            while x>0:
                res+=x%10
                x//=10
            if i == res:
                return i
        return -1
        
