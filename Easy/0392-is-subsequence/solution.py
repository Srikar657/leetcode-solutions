class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        r=0
        if not s:
            return True
        for i in range(len(t)):
            if s[r]==t[i]:
                r+=1
                if  r == len(s):
                    return True 
        return False
