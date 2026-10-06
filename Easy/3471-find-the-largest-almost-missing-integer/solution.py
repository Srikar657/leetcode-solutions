class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res=[]
        n=0
        i=k
        while i<=len(nums):
            res.append(nums[n:i])
            n+=1
            i+=1
        n,i=0,0
        nums=list(set(nums))
        nums=sorted(nums,reverse=True)
        out=[0]*len(nums)
        for i in nums:
            for j in res:
                if i in j:
                    out[n]+=1
            n+=1
        return nums[out.index(min(out))] if min(out)==1 else -1
