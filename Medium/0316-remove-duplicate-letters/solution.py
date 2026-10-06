class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last = {ch : i for i , ch in enumerate(s)}
        res =[]
        used = set()
        for i , ch in enumerate(s):
            if ch in used:
                continue
            while res and ch < res[-1] and i < last[res[-1]]:
                used.remove(res.pop())
            res.append(ch)
            used.add(ch)
        return "".join(res)
