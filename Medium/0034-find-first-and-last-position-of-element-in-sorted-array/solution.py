class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        if target not in nums or len(nums)==0:
            return [-1,-1]
        a=[]
        a.append(nums.index(target))
        b=nums[::-1]
        x=(len(nums)-1)-(b.index(target))
        a.append(x)
        return a
