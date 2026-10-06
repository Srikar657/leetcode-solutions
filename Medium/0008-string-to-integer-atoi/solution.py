class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s: return 0
        sign = -1 if s[0] == '-' else 1
        i = 1 if s[0] in '+-' else 0
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        num *= sign
        return max(-2**31, min(num, 2**31 - 1))
