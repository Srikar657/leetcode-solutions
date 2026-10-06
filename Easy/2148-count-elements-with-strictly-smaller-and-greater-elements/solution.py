class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mins=min(nums)
        maxs=max(nums)
        count=0
        for i in nums:
            if mins < i < maxs:
                count+=1
        return count
