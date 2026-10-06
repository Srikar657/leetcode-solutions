class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res="".join(map(str,digits))
        res=int(res)
        res+=1
        res=str(res)
        r=list(res)
        return [int(x) for x in r]
