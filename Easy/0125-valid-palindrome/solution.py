class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        t=""
        for i in s:
            if i.isalnum():
                t+=i
        if t == t[::-1]:
            return True
        return False
