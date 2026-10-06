class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        res = ""
        t = 0
        r = ""
        d = {k: v for k, v in knowledge}
        for i in s:
            if i == "(":
                r = ""
                t = 1
            elif i == ")":
                res += d.get(r, "?")
                t = 0
            elif t == 1:
                r += i
            else:
                res += i
        return res
