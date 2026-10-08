class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        c=0
        r=""
        for i in s:
            if i == "(":
                if c > 0:  
                    r += "("
                c += 1
            elif i == ")":
                c -= 1
                if c > 0: 
                    r += ")"
                if c == 0:
                    res.append(r)
                    r = ""
        return "".join(res)
