class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        for i in range(len(s)):
            if s[i] not in seen:
                if s.count(s[i])==1:
                    return i
            seen.add(s[i])
        return -1
        
