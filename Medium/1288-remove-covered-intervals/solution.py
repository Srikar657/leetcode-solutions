class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        t=sorted(intervals,key=lambda x: (x[0] , -x[1]))
        r=0
        m=0
        for i,j in t:
            if j>m:
                r+=1
                m=j
        return r
        
