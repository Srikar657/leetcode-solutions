class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=[]
        max_len=0
        for i in s:
            if i in count:
                while i in count:
                    count.pop(0)
            count.append(i)
            max_len=max(max_len, len(count))
        return max_len
