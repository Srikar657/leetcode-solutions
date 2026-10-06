class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num ==0:
            return "0"
        negative = num<0
        num =abs(num)
        x=num
        a=""
        while x:
            a=str(x%7)+a
            x=x//7
        return "-"+a if negative else a
