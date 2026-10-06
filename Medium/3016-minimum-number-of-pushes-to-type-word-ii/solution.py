from collections import Counter
class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq=Counter(word)
        counts=sorted(freq.values(),reverse=True)
        total_pushes=0
        for i ,c in enumerate(counts):
            cost=(i//8)+1
            total_pushes+=c*cost
        return total_pushes
