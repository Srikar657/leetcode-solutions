class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        s=sorted(d.items(),key=lambda x:x[1],reverse=True)
        b=[]
        for i in range(k):
            b.append(s[i][0])
        return b
