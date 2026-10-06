class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[0]
        for ch in s:
            if ch=='(':
                stack.append(0)
            else:
                v=stack.pop()
                if v==0:
                    stack[-1]+=1
                else:
                    stack[-1]+=2*v
        return stack[0]
