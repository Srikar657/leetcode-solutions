class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        c=0
        r = float('-inf')
        for i,j in intervals:
            if i>=r:
                r=j
            else:
                c+=1
        return c
