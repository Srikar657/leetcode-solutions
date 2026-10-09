class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        r=0
        c=0
        i=0
        while i < len(s):
            if s[i] == "(":
                r+=1
                i+=1
            else:
                if i+1 < len(s) and s[i+1] == ")":
                    if r >0:
                        r-=1
                    else:
                        c+=1
                    i+=2
                else:
                    if r > 0:
                        r-=1
                        c+=1
                    else:
                        c+=2
                    i+=1
        c+=2*r
        return c
