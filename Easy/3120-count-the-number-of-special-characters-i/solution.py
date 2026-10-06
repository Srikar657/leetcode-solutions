class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        low=set()
        high=set()
        for i in word:
            if i.islower():
                low.add(i)
            elif i.isupper():
                high.add(i)
        count=0
        for i in low:
            if i.upper() in high:
                count+=1
        return count
        
