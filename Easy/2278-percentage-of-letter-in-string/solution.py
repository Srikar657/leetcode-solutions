class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        res=s.count(letter)
        result=int((float(res)/len(s))*100)
        return result
