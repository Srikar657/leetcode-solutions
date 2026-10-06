class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        exp=sorted(heights)
        res=0
        for i in range(len(heights)):
            if heights[i]!=exp[i]:
                res+=1
        return res
