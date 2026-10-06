class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=""
        for t in range(len(min(strs,key=len))):
            char = strs[0][t]
            if all(s[t]==char for s in strs):
                res+=char
            else:
                return res
        return res
