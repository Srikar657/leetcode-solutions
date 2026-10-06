class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        res = set()
        n = len(digits)
        
        # Try all combinations of 3 digits
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:  
                        num = digits[i]*100 + digits[j]*10 + digits[k]
                        if num >= 100 and num % 2 == 0:
                            res.add(num)
        return len(res)
