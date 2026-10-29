class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        res=[]
        k=len(part)
        for i in s:
            res.append(i)
            if len(res)>=k and "".join(res[-k:]) == part:
                for j in range(k):
                    res.pop()
        return "".join(res)
