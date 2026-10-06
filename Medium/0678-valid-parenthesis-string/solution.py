class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = 0
        for i in s:
            if i == "(":
                l+= 1
                r+= 1
            elif i == ")":
                l-= 1
                r-= 1
            else: 
                l-= 1 
                r+= 1
            if r<0:
                return False
            if l<0:
                l= 0
        return l == 0
