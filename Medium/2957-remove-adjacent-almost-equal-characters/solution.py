class Solution(object):
    def removeAlmostEqualCharacters(self, word):
        """
        :type word: str
        :rtype: int
        """
        ops=0
        prev=None
        for ch in word:
            if prev is not None and (prev==ch or abs(ord(prev)-ord(ch))==1):
                ops+=1
                prev='#'
            else:
                prev=ch
        return ops      
