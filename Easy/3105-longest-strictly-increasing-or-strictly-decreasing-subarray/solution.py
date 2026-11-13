class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                res.append(nums[i:j+1])
        r=1
        for i in res:
            a=len(i)
            j=1
            inc=1
            dec=1
            while j!=a:
                if i[j-1] > i[j]:
                    dec+=1
                elif i[j-1]<i[j]:
                    inc+=1
                else:
                    break
                j+=1
            if inc == a or dec ==a:
                r = max(r,a)
        return r
