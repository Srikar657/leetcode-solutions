class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        n = len(s)
        for i in range(n):
            for j in range(i,n):
                ss=s[i:j+1]
                if ss==ss[::-1]:
                    res+=1
        return res
