class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        low =set()
        high=set()
        for i in word:
            if i.islower():
                low.add(i)
            elif i.isupper():
                high.add(i)
        count=0
        for i in low:
            upper_c=i.upper()
            if upper_c in high:
                last_lower=word.rfind(i)
                first_upper=word.find(upper_c)
                if last_lower !=-1 and first_upper !=-1 and last_lower<first_upper:
                    count+=1
        return count
