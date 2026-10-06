class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total = sum(nums)
        target = total - x
        if target == 0:
            return len(nums)
        res = 0
        i = 0
        j = 0
        n = 0
        s = 0
        while(n < len(nums)):
            s = s + nums[j]
            while(s > target and i <= j):
                s = s - nums[i]
                i += 1
            if s == target:
                if j - i + 1 > res:
                    res = j - i + 1
            j += 1
            n += 1
        if res == 0:
            return -1
        else:
            return len(nums) - res
