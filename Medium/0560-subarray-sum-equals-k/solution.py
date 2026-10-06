class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        prefix_sum=0
        freq={0:1}
        for num in nums:
            prefix_sum+=num
            if prefix_sum-k in freq:
                c+=freq[prefix_sum-k]
            freq[prefix_sum]=freq.get(prefix_sum,0)+1
        return c
