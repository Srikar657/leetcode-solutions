class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxs=0
        for i , jump in enumerate(nums):
            if i >maxs:
                return False
            maxs=max(maxs,i+jump)
        return True
