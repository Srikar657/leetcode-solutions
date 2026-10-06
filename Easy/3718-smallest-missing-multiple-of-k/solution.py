class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        r=0
        i=1
        while True:
            r=k*i
            i+=1
            if r not in nums:
                return r
