class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        l=0
        res=[]
        for i in seq:
            if i=="(":
                l+=1
                res.append(l%2)
            else:
                res.append(l%2)
                l-=1
        return res
