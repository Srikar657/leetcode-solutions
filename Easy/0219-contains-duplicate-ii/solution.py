class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        i = 0
        while i < len(nums):
            num = nums[i]
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
            i += 1
        return False
