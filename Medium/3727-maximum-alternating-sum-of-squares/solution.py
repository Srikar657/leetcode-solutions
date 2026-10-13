class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        for i in nums:
            res.append(i*i)
        i=0
        res.sort()
        j=len(res)-1
        r=0
        m=(i+j)//2
        if len(res)%2!=0:
            while (i<j and i<m):
                r+=res[j]
                r-=res[i]
                i+=1
                j-=1
            r+=res[j]
        else:
            while (i<=j):
                r+=res[j]
                r-=res[i]
                i+=1
                j-=1
        return r
