from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c=Counter(s)
        s=sorted(c.items(),key=lambda x:-x[1])
        return "".join(ch * freq for ch, freq in s)
