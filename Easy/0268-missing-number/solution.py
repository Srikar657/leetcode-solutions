class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h=max(nums)
        for i in range(0,h):
            if i not in nums:
                return i
        return h+1 if 0 in nums else 0
        
