class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c={}
        for i in nums:
            c[i]=c.get(i,0)+1
            if c[i]>len(nums)//2:
                return i
        
