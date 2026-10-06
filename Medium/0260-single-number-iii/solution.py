from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        c=Counter(nums)
        for i in nums:
            if c[i]==1:
                res.append(i)
            if len(res)==2:
                break
        return res
