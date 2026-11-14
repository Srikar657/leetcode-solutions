class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        arr=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                k=nums[i:j+1]
                if l <= len(k) <= r:
                    q=(sum(k))
                    if q >0:
                        arr.append(q)
        if len(arr)==0:
            return -1
        return min(arr)
